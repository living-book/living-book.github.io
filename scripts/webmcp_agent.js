#!/usr/bin/env node
/*
 * WebMCP agent harness: a real, foreign LLM drives the Concept Atlas
 * through the exact tools the page registers via document.modelContext.
 *
 * The page is the MCP server, this script is the transport, the LLM is
 * the client. No atlas knowledge is given to the model — only the tool
 * schemas the page itself registers.
 *
 * Providers:
 *   - ollama (default): local model, e.g. qwen2.5-coder:7b-64k
 *   - anthropic: used automatically when ANTHROPIC_API_KEY is set
 *
 * Usage:
 *   node scripts/webmcp_agent.js [--page 2d|3d] [--model NAME] [--headless]
 *                                [--port 8938] "your question"
 *
 * Requires playwright-core + a cached ms-playwright chromium. Override
 * the playwright-core location with PLAYWRIGHT_CORE if needed.
 */
const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');

const PW = process.env.PLAYWRIGHT_CORE ||
  '/home/sanjayg4/.hermes/hermes-agent/node_modules/playwright-core';
const { chromium } = require(PW);

/* ---------- args ---------- */
const argv = process.argv.slice(2);
const opt = { page: '3d', model: null, headless: false, port: 8938 };
const prompt = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i] === '--page') opt.page = argv[++i];
  else if (argv[i] === '--model') opt.model = argv[++i];
  else if (argv[i] === '--headless') opt.headless = true;
  else if (argv[i] === '--port') opt.port = +argv[++i];
  else prompt.push(argv[i]);
}
const QUESTION = prompt.join(' ') ||
  'What does this library say about habit formation? Any concepts that disagree with each other?';
const PROVIDER = process.env.ANTHROPIC_API_KEY ? 'anthropic' : 'ollama';
const MODEL = opt.model ||
  (PROVIDER === 'anthropic' ? 'claude-sonnet-5' : 'qwen2.5-coder:7b-64k');

/* ---------- find chromium ---------- */
const CACHE = path.join(process.env.HOME, '.cache/ms-playwright');
const dir = fs.readdirSync(CACHE)
  .filter(d => d.startsWith('chromium-') &&
    fs.existsSync(path.join(CACHE, d, 'chrome-linux/chrome')))
  .sort().pop();
const EXE = path.join(CACHE, dir, 'chrome-linux/chrome');

/* ---------- stub: collect what the page registers ---------- */
const STUB = `
  window.__mcpTools = [];
  Object.defineProperty(document, 'modelContext', {
    configurable: true,
    value: { registerTool: t => { window.__mcpTools.push(t); return Promise.resolve(); } },
  });
`;

/* ---------- providers ---------- */
async function askOllama(messages, tools) {
  const res = await fetch('http://localhost:11434/api/chat', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      model: MODEL, stream: false, messages,
      tools: tools.map(t => ({
        type: 'function',
        function: { name: t.name, description: t.description, parameters: t.inputSchema },
      })),
    }),
  });
  if (!res.ok) throw new Error('ollama ' + res.status + ': ' + await res.text());
  const m = (await res.json()).message;
  let text = m.content || '';
  let calls = (m.tool_calls || []).map(c => ({ name: c.function.name, args: c.function.arguments || {} }));
  // small local models often emit the call as JSON text instead of tool_calls
  if (!calls.length) {
    const j = text.match(/\{[\s\S]*\}/);
    if (j) {
      try {
        const o = JSON.parse(j[0]);
        if (o.name) { calls = [{ name: o.name, args: o.arguments || o.args || {} }]; text = ''; }
      } catch (e) {}
    }
  }
  return { text, calls, raw: m };
}

async function askAnthropic(messages, tools) {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      'x-api-key': process.env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model: MODEL, max_tokens: 1500,
      system: messages.find(m => m.role === 'system')?.content,
      messages: messages.filter(m => m.role !== 'system'),
      tools: tools.map(t => ({ name: t.name, description: t.description, input_schema: t.inputSchema })),
    }),
  });
  if (!res.ok) throw new Error('anthropic ' + res.status + ': ' + await res.text());
  const body = await res.json();
  return {
    text: body.content.filter(b => b.type === 'text').map(b => b.text).join('\n'),
    calls: body.content.filter(b => b.type === 'tool_use')
      .map(b => ({ name: b.name, args: b.input, id: b.id })),
    raw: { role: 'assistant', content: body.content },
  };
}

/* ---------- main ---------- */
(async () => {
  const DOCS = path.join(__dirname, '..', 'docs');
  const server = spawn('python3', ['-m', 'http.server', String(opt.port), '-d', DOCS],
    { stdio: 'ignore' });
  const kill = () => { try { server.kill(); } catch (e) {} };
  process.on('exit', kill);

  const outDir = process.env.WEBMCP_OUT || path.join(require('os').tmpdir(), 'webmcp-agent');
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch({
    executablePath: EXE, headless: opt.headless,
    args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--no-sandbox'],
  });
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 880 },
    recordVideo: { dir: outDir, size: { width: 1440, height: 880 } },
  });
  await ctx.addInitScript(STUB);
  const page = await ctx.newPage();

  const url = `http://localhost:${opt.port}/atlas/${opt.page === '3d' ? '3d/' : ''}`;
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForFunction(() => window.__mcpTools.length >= 6, null, { timeout: 30000 });

  const tools = await page.evaluate(() =>
    window.__mcpTools.map(t => ({ name: t.name, description: t.description, inputSchema: t.inputSchema })));

  console.log(`page: ${url}`);
  console.log(`provider: ${PROVIDER} / ${MODEL}`);
  console.log(`tools registered by page: ${tools.map(t => t.name).join(', ')}\n`);
  console.log(`Q: ${QUESTION}\n${'='.repeat(70)}`);

  const SYSTEM =
    'You are an AI agent operating a live web page called the Concept Atlas — a map of ' +
    'concepts extracted from a personal library of books, linked by typed edges ' +
    '(extends, contradicts, tempers, parallels, instantiates, formalizes). ' +
    'You know nothing about its contents except what the tools return. ' +
    'Answer the user by calling tools. Prefer find_concepts first to discover ids. ' +
    'Use focus_concept to visually show the user what you are talking about. ' +
    'When you have enough information, stop calling tools and write a final answer ' +
    'IN YOUR OWN WORDS (3-6 sentences) summarizing what the tools returned. ' +
    'Never repeat a tool result verbatim as your answer.';

  const messages = [
    { role: 'system', content: SYSTEM },
    { role: 'user', content: QUESTION },
  ];
  const ask = PROVIDER === 'anthropic' ? askAnthropic : askOllama;
  const transcript = [`# WebMCP agent run\n\npage: ${url}\nprovider: ${PROVIDER} / ${MODEL}\n\n**Q: ${QUESTION}**\n`];

  let finalText = '';
  for (let turn = 1; turn <= 12; turn++) {
    const { text, calls, raw } = await ask(messages, tools);
    messages.push(raw);
    if (text) console.log(`\n[model] ${text}`);
    if (!calls.length) { finalText = text; break; }

    const results = [];
    for (const c of calls) {
      console.log(`\n[tool→] ${c.name}(${JSON.stringify(c.args)})`);
      transcript.push(`- \`${c.name}(${JSON.stringify(c.args)})\``);
      let out;
      try {
        out = await page.evaluate(async ({ name, args }) => {
          const t = window.__mcpTools.find(t => t.name === name);
          return t ? String(await t.execute(args || {})) : 'unknown tool: ' + name;
        }, c);
      } catch (e) { out = 'tool error: ' + e.message; }
      console.log(`[tool←] ${out.split('\n').slice(0, 6).join('\n        ')}${out.split('\n').length > 6 ? '\n        …' : ''}`);
      transcript.push('```\n' + out + '\n```');
      results.push({ call: c, out });
      // let the camera move finish so a human (and the video) can see it
      if (/focus_concept|tension_lens|reset_view/.test(c.name)) await page.waitForTimeout(1800);
    }

    if (PROVIDER === 'anthropic') {
      messages.push({
        role: 'user',
        content: results.map(r => ({ type: 'tool_result', tool_use_id: r.call.id, content: r.out })),
      });
    } else {
      for (const r of results) messages.push({ role: 'tool', content: r.out });
    }
  }

  console.log('\n' + '='.repeat(70));
  console.log(finalText ? `FINAL ANSWER:\n${finalText}` : 'No final answer (turn limit hit).');
  transcript.push(`\n**Final answer:**\n\n${finalText || '_turn limit hit_'}`);

  await page.waitForTimeout(1500);
  const video = page.video();
  await ctx.close();
  const vpath = video ? await video.path() : null;
  await browser.close();
  kill();

  const tpath = path.join(outDir, 'transcript.md');
  fs.writeFileSync(tpath, transcript.join('\n'));
  console.log(`\ntranscript: ${tpath}`);
  if (vpath) console.log(`video: ${vpath}`);
  process.exit(finalText ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
