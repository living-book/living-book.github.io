/* WebMCP tools for the Concept Atlas (2D + 3D views).
   Exposes the atlas — concepts, verified edges, graph traversal, and view
   control — as callable tools for in-browser AI agents via the WebMCP
   origin trial (Chrome 149–156): document.modelContext.registerTool.

   Each atlas page calls window.AtlasMCP(hooks) once its data is loaded:
     hooks = {
       data,            // parsed atlas.json
       page,            // '2d' | '3d'
       focus(id, depth) // select a concept in the view
       reset()          // clear selection
       lens(on)         // 3d only: tension lens on/off
     }
   Silently no-ops in browsers without WebMCP. */
(function () {
  'use strict';

  window.AtlasMCP = function (hooks) {
    var mc = document.modelContext || navigator.modelContext;
    if (mc && !mc.registerTool) mc = null;
    var demoMode = /[?&]demo\b/.test(location.search);
    if (!mc && !demoMode) return;

    var data = hooks.data;
    var byId = {}, bookBy = {}, adj = {};
    data.books.forEach(function (b) { bookBy[b.slug] = b; });
    data.concepts.forEach(function (c) { byId[c.id] = c; adj[c.id] = []; });
    var edges = data.edges.filter(function (e) { return byId[e.from] && byId[e.to]; });
    edges.forEach(function (e) { adj[e.from].push(e); adj[e.to].push(e); });
    var TENSION = { tempers: 1, contradicts: 1 };

    function domainOf(c) { return (bookBy[c.book] || {}).domain || 'unknown'; }
    function bookTitle(c) { return (bookBy[c.book] || {}).title || c.book; }
    function head(c) {
      return c.title + ' [' + c.id + '] — from "' + bookTitle(c) + '" (' +
        domainOf(c) + '), ' + adj[c.id].length + ' connections';
    }
    function edgeLine(e) {
      return byId[e.from].title + ' —' + e.verb + '→ ' + byId[e.to].title +
        (e.why ? ': ' + e.why : '');
    }

    /* fuzzy scorer shared by search + name resolution */
    function scoreAll(query) {
      var q = query.toLowerCase().trim();
      var toks = q.match(/[a-z][a-z-]+/g) || [];
      return data.concepts.map(function (c) {
        var title = c.title.toLowerCase(), s = 0;
        if (c.id === q) s += 100;
        if (title === q) s += 60;
        else if (title.indexOf(q) >= 0) s += 25;
        var hay = title + ' ' + (c.description || '').toLowerCase() + ' ' +
          (c.tags || []).join(' ').toLowerCase();
        toks.forEach(function (t) {
          if (title.indexOf(t) >= 0) s += 6;
          else if (hay.indexOf(t) >= 0) s += 2;
        });
        return [s, c];
      }).filter(function (x) { return x[0] > 0; })
        .sort(function (a, b) { return b[0] - a[0] || adj[b[1].id].length - adj[a[1].id].length; });
    }

    /* resolve a user/agent-supplied name to one concept, or explain the miss */
    function resolve(name) {
      if (byId[name]) return { c: byId[name] };
      var hits = scoreAll(name);
      if (hits.length && (hits[0][0] >= 25 || hits.length === 1)) return { c: hits[0][1] };
      var near = hits.slice(0, 5).map(function (x) { return x[1].title + ' [' + x[1].id + ']'; });
      return { err: 'No concept matches "' + name + '".' +
        (near.length ? ' Closest: ' + near.join('; ') : ' Try find_concepts first.') };
    }

    /* unweighted shortest path over the edge graph */
    function shortestPath(fromId, toId) {
      var prev = {}; prev[fromId] = null;
      var queue = [fromId];
      while (queue.length) {
        var id = queue.shift();
        if (id === toId) break;
        var es = adj[id];
        for (var i = 0; i < es.length; i++) {
          var e = es[i], nb = e.from === id ? e.to : e.from;
          if (!(nb in prev)) { prev[nb] = { id: id, e: e }; queue.push(nb); }
        }
      }
      if (!(toId in prev)) return null;
      var steps = [], cur = toId;
      while (prev[cur]) { steps.unshift(prev[cur].e); cur = prev[cur].id; }
      return steps;
    }

    /* ---- toast: make agent tool calls visible to the human watching ---- */
    var box = document.createElement('div');
    box.style.cssText = 'position:fixed;left:50%;bottom:24px;transform:translateX(-50%);' +
      'z-index:99;display:flex;flex-direction:column-reverse;gap:6px;align-items:center;' +
      'pointer-events:none;';
    document.body.appendChild(box);
    function toast(msg) {
      var t = document.createElement('div');
      t.textContent = msg;
      t.style.cssText = 'background:rgba(28,27,24,.95);color:#f5f4ed;border:1px solid #d97757;' +
        'border-radius:999px;padding:7px 16px;font:12.5px system-ui,sans-serif;' +
        'box-shadow:0 4px 24px rgba(0,0,0,.35);max-width:80vw;white-space:nowrap;' +
        'overflow:hidden;text-overflow:ellipsis;transition:opacity .5s;';
      box.appendChild(t);
      setTimeout(function () { t.style.opacity = '0'; }, 3200);
      setTimeout(function () { t.remove(); }, 3800);
    }

    /* ---- tool registry ---- */
    var registered = [];
    function tool(def, readOnly) {
      var exec = def.execute;
      def.execute = function (input) {
        toast('🤖 ' + def.name + '(' + JSON.stringify(input || {}).slice(0, 60) + ')');
        return Promise.resolve().then(function () { return exec(input || {}); });
      };
      def.annotations = { readOnlyHint: !!readOnly };
      registered.push(def);
      if (!mc) return;
      var p = mc.registerTool(def);
      if (p && p.catch) p.catch(function () {});
    }

    var stats = data.books.length + ' books, ' + data.concepts.length +
      ' concepts, ' + edges.length + ' human-verified cross-book edges';

    tool({
      name: 'find_concepts',
      description: 'Search the Living Books Concept Atlas (' + stats + ') by keyword or ' +
        'theme. Returns matching concepts with their id (slug), source book, domain, and ' +
        'connection count. Use the returned id with get_concept, focus_concept, or connect_concepts.',
      inputSchema: {
        type: 'object',
        properties: {
          query: { type: 'string', description: 'Keywords, a concept name, or a theme' },
          limit: { type: 'number', description: 'Max results, default 8' },
        },
        required: ['query'],
      },
      execute: function (a) {
        var hits = scoreAll(a.query).slice(0, a.limit || 8);
        if (!hits.length) return 'No concepts match "' + a.query + '".';
        return hits.map(function (x) {
          return head(x[1]) + '\n  ' + (x[1].description || '');
        }).join('\n');
      },
    }, true);

    tool({
      name: 'get_concept',
      description: 'Full detail for one atlas concept: definition, why it matters, and every ' +
        'verified connection to other books grouped by relationship verb (extends, contradicts, ' +
        'tempers, formalizes, instantiates, parallels), each with a one-sentence justification.',
      inputSchema: {
        type: 'object',
        properties: { concept: { type: 'string', description: 'Concept id (slug) or title' } },
        required: ['concept'],
      },
      execute: function (a) {
        var r = resolve(a.concept);
        if (r.err) return r.err;
        var c = r.c;
        var out = [head(c), '', c.definition || c.description || ''];
        if (c.whyItMatters) out.push('', 'Why it matters: ' + c.whyItMatters);
        var groups = {};
        adj[c.id].forEach(function (e) { (groups[e.verb] = groups[e.verb] || []).push(e); });
        ['contradicts', 'tempers', 'formalizes', 'extends', 'instantiates', 'parallels']
          .forEach(function (v) {
            if (!groups[v]) return;
            out.push('', v.toUpperCase() + ' (' + groups[v].length + '):');
            groups[v].forEach(function (e) { out.push('- ' + edgeLine(e)); });
          });
        return out.join('\n');
      },
    }, true);

    tool({
      name: 'connect_concepts',
      description: 'Find the shortest chain of verified relationships linking two concepts ' +
        'across the atlas — how an idea in one book reaches an idea in another. Returns each ' +
        'hop with its relationship verb and justification.',
      inputSchema: {
        type: 'object',
        properties: {
          from: { type: 'string', description: 'Start concept id or title' },
          to: { type: 'string', description: 'End concept id or title' },
        },
        required: ['from', 'to'],
      },
      execute: function (a) {
        var rf = resolve(a.from), rt = resolve(a.to);
        if (rf.err) return rf.err;
        if (rt.err) return rt.err;
        if (rf.c.id === rt.c.id) return 'Those resolve to the same concept: ' + head(rf.c);
        var steps = shortestPath(rf.c.id, rt.c.id);
        if (!steps) return 'No path between ' + rf.c.title + ' and ' + rt.c.title +
          ' — they live in disconnected parts of the atlas.';
        var out = [rf.c.title + ' → ' + rt.c.title + ' in ' + steps.length + ' hop' +
          (steps.length > 1 ? 's' : '') + ':'];
        steps.forEach(function (e, i) { out.push((i + 1) + '. ' + edgeLine(e)); });
        out.push('', 'Tip: call focus_concept on any id to see it in the 3D galaxy.');
        return out.join('\n');
      },
    }, true);

    tool({
      name: 'list_tensions',
      description: 'List places where books genuinely disagree: "contradicts" and "tempers" ' +
        'edges, each with a one-sentence justification. Optionally filter by domain (' +
        Object.keys(DOMAINS()).join('; ') + ') or around one concept.',
      inputSchema: {
        type: 'object',
        properties: {
          domain: { type: 'string', description: 'Optional domain filter (substring ok)' },
          concept: { type: 'string', description: 'Optional: only tensions touching this concept' },
          limit: { type: 'number', description: 'Max results, default 10' },
        },
      },
      execute: function (a) {
        var pool = edges.filter(function (e) { return TENSION[e.verb]; });
        if (a.concept) {
          var r = resolve(a.concept);
          if (r.err) return r.err;
          pool = pool.filter(function (e) { return e.from === r.c.id || e.to === r.c.id; });
        }
        if (a.domain) {
          var q = a.domain.toLowerCase();
          pool = pool.filter(function (e) {
            return domainOf(byId[e.from]).toLowerCase().indexOf(q) >= 0 ||
                   domainOf(byId[e.to]).toLowerCase().indexOf(q) >= 0;
          });
        }
        if (!pool.length) return 'No tensions match that filter.';
        var lim = a.limit || 10;
        var out = pool.slice(0, lim).map(function (e) {
          return '[' + e.verb + '] ' + edgeLine(e) + '  (ids: ' + e.from + ', ' + e.to + ')';
        });
        if (pool.length > lim) out.push('…and ' + (pool.length - lim) + ' more.');
        return out.join('\n');
      },
    }, true);

    tool({
      name: 'focus_concept',
      description: 'Visually focus a concept in the atlas the user is looking at' +
        (hooks.page === '3d'
          ? ' — the 3D galaxy spins until that node faces the viewer, then shows only its neighborhood.'
          : ' — selects it on the map and opens its card.') +
        ' Use after find_concepts or connect_concepts to show the user what you are talking about.',
      inputSchema: {
        type: 'object',
        properties: {
          concept: { type: 'string', description: 'Concept id (slug) or title' },
          depth: { type: 'number', description: '3D only: neighborhood hops to keep visible, 1-3 (default 2)' },
        },
        required: ['concept'],
      },
      execute: function (a) {
        var r = resolve(a.concept);
        if (r.err) return r.err;
        hooks.focus(r.c.id, a.depth);
        return 'Focused ' + head(r.c) + '. The view now centers on it.';
      },
    });

    if (hooks.lens) tool({
      name: 'tension_lens',
      description: 'Toggle the 3D tension lens: when on, only "contradicts" and "tempers" ' +
        'edges glow — the disagreement skeleton of the whole library.',
      inputSchema: {
        type: 'object',
        properties: { on: { type: 'boolean', description: 'true = show only tensions' } },
        required: ['on'],
      },
      execute: function (a) { hooks.lens(!!a.on); return 'Tension lens ' + (a.on ? 'on' : 'off') + '.'; },
    });

    tool({
      name: 'reset_view',
      description: 'Clear the current selection and return the atlas view to the full graph.',
      inputSchema: { type: 'object', properties: {} },
      execute: function () { hooks.reset(); return 'View reset to the full atlas.'; },
    });

    function DOMAINS() {
      var d = {};
      data.books.forEach(function (b) { if (b.domain) d[b.domain] = 1; });
      return d;
    }

    if (mc) toast('🤖 ' + registered.length + ' atlas tools registered for AI agents');

    /* ---- ?demo — replay a scripted agent session through the same tools,
       so the actuation is visible even without a WebMCP-enabled agent ---- */
    function call(name, args) {
      var d = registered.filter(function (t) { return t.name === name; })[0];
      return d ? d.execute(args) : Promise.resolve('');
    }
    function sleep(ms) { return new Promise(function (res) { setTimeout(res, ms); }); }
    async function tour() {
      toast('🎬 WebMCP demo — replaying an AI-agent session against the atlas tools');
      await sleep(2400);
      toast('🤖 agent: “Where does this library disagree with itself?”');
      await sleep(1800);
      await call('list_tensions', { limit: 3 });
      await sleep(2600);
      if (hooks.lens) {
        await call('tension_lens', { on: true });
        await sleep(4000);
        await call('tension_lens', { on: false });
        await sleep(1200);
      }
      toast('🤖 agent: “Connect feedback loops to habit formation.”');
      await sleep(1800);
      await call('connect_concepts', { from: 'feedback-loops', to: 'identity-based-habits' });
      await sleep(1800);
      var steps = shortestPath('feedback-loops', 'identity-based-habits') || [];
      var walk = ['feedback-loops'];
      steps.forEach(function (e) { walk.push(walk[walk.length - 1] === e.from ? e.to : e.from); });
      for (var i = 0; i < walk.length; i++) {
        await call('focus_concept', { concept: walk[i], depth: 1 });
        if (steps[i]) { await sleep(900); toast('↳ ' + edgeLine(steps[i]).slice(0, 110)); }
        await sleep(2400);
      }
      await call('reset_view', {});
      toast('✨ Demo over — same tools are live for AI agents via the WebMCP origin trial.');
    }
    if (demoMode) setTimeout(function () { tour().catch(function () {}); },
      hooks.page === '3d' ? 2600 : 1400);
  };
})();
