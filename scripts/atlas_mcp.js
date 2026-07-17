#!/usr/bin/env node
/*
 * atlas-mcp: the Concept Atlas as a real MCP stdio server.
 *
 * Same read tools the atlas pages register in the browser via WebMCP
 * (docs/atlas/webmcp.js), minus the view-actuation ones — there is no
 * view here. Zero dependencies: raw JSON-RPC 2.0 over newline-delimited
 * stdio, per the MCP stdio transport.
 *
 * Register with Claude Code:
 *   claude mcp add atlas -- node /path/to/scripts/atlas_mcp.js
 * or use the repo's .mcp.json.
 *
 * ATLAS_JSON overrides the atlas.json location (default: ../docs/atlas/atlas.json).
 */
'use strict';
const fs = require('fs');
const path = require('path');
const readline = require('readline');

/* ---------- data (same indexes webmcp.js builds) ---------- */
const ATLAS = process.env.ATLAS_JSON ||
  path.join(__dirname, '..', 'docs', 'atlas', 'atlas.json');
const data = JSON.parse(fs.readFileSync(ATLAS, 'utf8'));

const byId = {}, bookBy = {}, adj = {};
data.books.forEach(b => { bookBy[b.slug] = b; });
data.concepts.forEach(c => { byId[c.id] = c; adj[c.id] = []; });
const edges = data.edges.filter(e => byId[e.from] && byId[e.to]);
edges.forEach(e => { adj[e.from].push(e); adj[e.to].push(e); });
const TENSION = { tempers: 1, contradicts: 1 };

const domainOf = c => (bookBy[c.book] || {}).domain || 'unknown';
const bookTitle = c => (bookBy[c.book] || {}).title || c.book;
const head = c => `${c.title} [${c.id}] — from "${bookTitle(c)}" (${domainOf(c)}), ${adj[c.id].length} connections`;
const edgeLine = e => `${byId[e.from].title} —${e.verb}→ ${byId[e.to].title}${e.why ? ': ' + e.why : ''}`;

function scoreAll(query) {
  const q = query.toLowerCase().trim();
  const toks = q.match(/[a-z][a-z-]+/g) || [];
  return data.concepts.map(c => {
    const title = c.title.toLowerCase();
    let s = 0;
    if (c.id === q) s += 100;
    if (title === q) s += 60;
    else if (title.includes(q)) s += 25;
    const hay = title + ' ' + (c.description || '').toLowerCase() + ' ' +
      (c.tags || []).join(' ').toLowerCase();
    for (const t of toks) {
      if (title.includes(t)) s += 6;
      else if (hay.includes(t)) s += 2;
    }
    return [s, c];
  }).filter(x => x[0] > 0)
    .sort((a, b) => b[0] - a[0] || adj[b[1].id].length - adj[a[1].id].length);
}

function resolve(name) {
  if (byId[name]) return { c: byId[name] };
  const hits = scoreAll(name);
  if (hits.length && (hits[0][0] >= 25 || hits.length === 1)) return { c: hits[0][1] };
  const near = hits.slice(0, 5).map(x => `${x[1].title} [${x[1].id}]`);
  return { err: `No concept matches "${name}".` +
    (near.length ? ' Closest: ' + near.join('; ') : ' Try find_concepts first.') };
}

function shortestPath(fromId, toId) {
  const prev = { [fromId]: null };
  const queue = [fromId];
  while (queue.length) {
    const id = queue.shift();
    if (id === toId) break;
    for (const e of adj[id]) {
      const nb = e.from === id ? e.to : e.from;
      if (!(nb in prev)) { prev[nb] = { id, e }; queue.push(nb); }
    }
  }
  if (!(toId in prev)) return null;
  const steps = [];
  let cur = toId;
  while (prev[cur]) { steps.unshift(prev[cur].e); cur = prev[cur].id; }
  return steps;
}

/* ---------- tools ---------- */
const stats = `${data.books.length} books, ${data.concepts.length} concepts, ${edges.length} human-verified cross-book edges`;
const domains = [...new Set(data.books.map(b => b.domain).filter(Boolean))];

const TOOLS = [
  {
    name: 'find_concepts',
    description: `Search the Living Books Concept Atlas (${stats}) by keyword or theme. ` +
      'Returns matching concepts with their id (slug), source book, domain, and connection ' +
      'count. Use the returned id with get_concept or connect_concepts.',
    inputSchema: {
      type: 'object',
      properties: {
        query: { type: 'string', description: 'Keywords, a concept name, or a theme' },
        limit: { type: 'number', description: 'Max results, default 8' },
      },
      required: ['query'],
    },
    execute(a) {
      const hits = scoreAll(a.query).slice(0, a.limit || 8);
      if (!hits.length) return `No concepts match "${a.query}".`;
      return hits.map(x => head(x[1]) + '\n  ' + (x[1].description || '')).join('\n');
    },
  },
  {
    name: 'get_concept',
    description: 'Full detail for one atlas concept: definition, why it matters, and every ' +
      'verified connection to other books grouped by relationship verb (extends, contradicts, ' +
      'tempers, formalizes, instantiates, parallels), each with a one-sentence justification.',
    inputSchema: {
      type: 'object',
      properties: { concept: { type: 'string', description: 'Concept id (slug) or title' } },
      required: ['concept'],
    },
    execute(a) {
      const r = resolve(a.concept);
      if (r.err) return r.err;
      const c = r.c;
      const out = [head(c), '', c.definition || c.description || ''];
      if (c.whyItMatters) out.push('', 'Why it matters: ' + c.whyItMatters);
      const groups = {};
      adj[c.id].forEach(e => { (groups[e.verb] = groups[e.verb] || []).push(e); });
      for (const v of ['contradicts', 'tempers', 'formalizes', 'extends', 'instantiates', 'parallels']) {
        if (!groups[v]) continue;
        out.push('', `${v.toUpperCase()} (${groups[v].length}):`);
        groups[v].forEach(e => out.push('- ' + edgeLine(e)));
      }
      return out.join('\n');
    },
  },
  {
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
    execute(a) {
      const rf = resolve(a.from), rt = resolve(a.to);
      if (rf.err) return rf.err;
      if (rt.err) return rt.err;
      if (rf.c.id === rt.c.id) return 'Those resolve to the same concept: ' + head(rf.c);
      const steps = shortestPath(rf.c.id, rt.c.id);
      if (!steps) return `No path between ${rf.c.title} and ${rt.c.title} — they live in disconnected parts of the atlas.`;
      const out = [`${rf.c.title} → ${rt.c.title} in ${steps.length} hop${steps.length > 1 ? 's' : ''}:`];
      steps.forEach((e, i) => out.push(`${i + 1}. ${edgeLine(e)}`));
      return out.join('\n');
    },
  },
  {
    name: 'list_tensions',
    description: 'List places where books genuinely disagree: "contradicts" and "tempers" ' +
      'edges, each with a one-sentence justification. Optionally filter by domain (' +
      domains.join('; ') + ') or around one concept.',
    inputSchema: {
      type: 'object',
      properties: {
        domain: { type: 'string', description: 'Optional domain filter (substring ok)' },
        concept: { type: 'string', description: 'Optional: only tensions touching this concept' },
        limit: { type: 'number', description: 'Max results, default 10' },
      },
    },
    execute(a) {
      let pool = edges.filter(e => TENSION[e.verb]);
      if (a.concept) {
        const r = resolve(a.concept);
        if (r.err) return r.err;
        pool = pool.filter(e => e.from === r.c.id || e.to === r.c.id);
      }
      if (a.domain) {
        const q = a.domain.toLowerCase();
        pool = pool.filter(e =>
          domainOf(byId[e.from]).toLowerCase().includes(q) ||
          domainOf(byId[e.to]).toLowerCase().includes(q));
      }
      if (!pool.length) return 'No tensions match that filter.';
      const lim = a.limit || 10;
      const out = pool.slice(0, lim).map(e => `[${e.verb}] ${edgeLine(e)}  (ids: ${e.from}, ${e.to})`);
      if (pool.length > lim) out.push(`…and ${pool.length - lim} more.`);
      return out.join('\n');
    },
  },
];
const toolBy = Object.fromEntries(TOOLS.map(t => [t.name, t]));

/* ---------- JSON-RPC over stdio ---------- */
const send = msg => process.stdout.write(JSON.stringify(msg) + '\n');

function handle(req) {
  const { id, method, params } = req;
  if (method === 'initialize') {
    return send({
      jsonrpc: '2.0', id,
      result: {
        protocolVersion: (params && params.protocolVersion) || '2025-06-18',
        capabilities: { tools: {} },
        serverInfo: { name: 'atlas-mcp', title: 'Living Books Concept Atlas', version: '1.0.0' },
        instructions: 'Read-only access to the Living Books Concept Atlas: ' + stats + '. ' +
          'Start with find_concepts to discover ids.',
      },
    });
  }
  if (method === 'ping') return send({ jsonrpc: '2.0', id, result: {} });
  if (method === 'tools/list') {
    return send({
      jsonrpc: '2.0', id,
      result: {
        tools: TOOLS.map(t => ({
          name: t.name, description: t.description, inputSchema: t.inputSchema,
          annotations: { readOnlyHint: true },
        })),
      },
    });
  }
  if (method === 'tools/call') {
    const t = toolBy[params && params.name];
    if (!t) return send({ jsonrpc: '2.0', id, error: { code: -32602, message: 'Unknown tool: ' + (params && params.name) } });
    let text, isError = false;
    try { text = String(t.execute(params.arguments || {})); }
    catch (e) { text = 'tool error: ' + e.message; isError = true; }
    return send({ jsonrpc: '2.0', id, result: { content: [{ type: 'text', text }], isError } });
  }
  // notifications (no id) are fire-and-forget; unknown requests get an error
  if (id !== undefined) {
    send({ jsonrpc: '2.0', id, error: { code: -32601, message: 'Method not found: ' + method } });
  }
}

readline.createInterface({ input: process.stdin, terminal: false })
  .on('line', line => {
    line = line.trim();
    if (!line) return;
    let req;
    try { req = JSON.parse(line); } catch (e) { return; }
    try { handle(req); }
    catch (e) {
      if (req.id !== undefined) {
        send({ jsonrpc: '2.0', id: req.id, error: { code: -32603, message: e.message } });
      }
    }
  });
