/** Local agent evaluation adapter. Never exposes the filesystem or vector bank.
 * Build (from worker/): node_modules/.bin/esbuild probe-kernel/agent-journey.ts
 *   --bundle --platform=node --format=esm --outfile=/tmp/agent-journey.mjs
 * Run from worker/: node /tmp/agent-journey.mjs --assets ../full-probe-reports/replay/runtime
 *   --manifest-sha SHA --query-vectors ../full-probe-reports/replay/query-vectors.f32
 *   --query-metadata ../full-probe-reports/replay/query-vectors.f32.json
 *   --sessions /tmp/sessions.json --out /tmp/journeys --port 8765
 * Registry: {sessions:[{id,question_id,question,vector_row}]} (or the array).
 * Registry row selection is trusted evaluator input; gold fields are rejected.
 */
import assert from 'node:assert/strict'
import { AsyncLocalStorage } from 'node:async_hooks'
import { createHash } from 'node:crypto'
import { appendFileSync, createReadStream, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { realpath, stat } from 'node:fs/promises'
import { createServer, type Server } from 'node:http'
import { isAbsolute, relative, resolve, sep } from 'node:path'
import { performance } from 'node:perf_hooks'
import { Readable } from 'node:stream'
import { pathToFileURL } from 'node:url'
import { createFullCorpusStoreLoader } from '../src/full-corpus-store'
import { createBoundedProbeHandler } from '../src/probe-admission'
import { createService } from '../src/service'
import { embed, pointLength, WordPieceTokenizer } from '../src/tokenize'

export interface JourneySession {
  id: string
  question_id: string
  question: string
  vector_row: number
}
export const JOURNEY_LIMITS = Object.freeze({ calls: 8, code_points: 48000 })
const SESSION_ID = /^[a-zA-Z0-9_-]{1,100}$/
const REST_FIELDS: Record<string, string[]> = {
  '/v1/search': ['q', 'k'], '/v1/catalog': ['q', 'section', 'offset', 'limit', 'version'],
  '/v1/paper': ['id'], '/v1/contents': ['id', 'version'],
  '/v1/find': ['id', 'q', 'offset', 'version'],
  '/v1/content': ['id', 'offset', 'length', 'version'],
  '/v1/citations': ['id', 'dir', 'limit', 'cursor'],
  '/v1/traverse': ['id', 'dir', 'hops', 'max_nodes'],
}
const MCP_FIELDS: Record<string, string[]> = { search: ['query'], fetch: ['id'] }
const EXHAUSTED = JSON.stringify({ error: { code: 'budget_exhausted' } })
const hash = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex')
const object = (value: unknown): value is Record<string, unknown> =>
  value !== null && typeof value === 'object' && !Array.isArray(value)
const onlyKeys = (value: Record<string, unknown>, keys: string[]) =>
  Object.keys(value).every((key) => keys.includes(key))
const json = (value: unknown, status = 200) => new Response(JSON.stringify(value), {
  status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
})
const error = (code: string, status = 400) => json({ error: { code } }, status)

export function parseSessions(value: unknown, vectorCount: number): JourneySession[] {
  if (object(value)) {
    assert(onlyKeys(value, ['sessions']), 'Unknown registry fields (gold/answers are forbidden)')
    value = value.sessions
  }
  assert(Array.isArray(value) && value.length > 0, 'Nonempty session array required')
  const seen = new Set<string>()
  return value.map((row) => {
    assert(object(row) && onlyKeys(row, ['id', 'question_id', 'question', 'vector_row']),
      'Unknown session fields (gold/answers are forbidden)')
    assert(typeof row.id === 'string' && SESSION_ID.test(row.id) && !seen.has(row.id), 'Invalid/duplicate session id')
    assert(typeof row.question_id === 'string' && row.question_id.length > 0, 'Missing question id')
    assert(typeof row.question === 'string' && row.question.trim().length > 0
      && pointLength(row.question) <= 2000, 'Missing/invalid exact question')
    assert(Number.isSafeInteger(row.vector_row) && Number(row.vector_row) >= 0
      && Number(row.vector_row) < vectorCount, 'Missing/out-of-range saved query vector')
    seen.add(row.id)
    return Object.freeze({ id: row.id, question_id: row.question_id,
      question: row.question, vector_row: Number(row.vector_row) })
  })
}

export function readQueryBank(bytes: Buffer, metadata: Record<string, any>, manifest: Record<string, any>) {
  assert(metadata.dtype === 'float32' && metadata.byte_order === 'little', 'Unsupported saved query format')
  assert(metadata.dimensions === embed.dimensions && Number.isSafeInteger(metadata.count)
    && metadata.count > 0, 'Saved query dimensions/count mismatch')
  assert(metadata.query_template === embed.query_template, 'Saved query template differs from runtime')
  assert(metadata.encoder?.embedding_signature === manifest.embedding_signature,
    'Saved query embedding signature differs from corpus')
  assert(bytes.length === metadata.count * metadata.dimensions * 4, 'Saved query bytes missing')
  assert(hash(bytes) === metadata.vectors_sha256, 'Saved query checksum mismatch')
  return {
    count: metadata.count as number,
    vector(row: number) {
      assert(Number.isSafeInteger(row) && row >= 0 && row < metadata.count, 'Missing saved query vector')
      const values = Array.from({ length: metadata.dimensions }, (_, column) =>
        bytes.readFloatLE((row * metadata.dimensions + column) * 4))
      assert(values.every(Number.isFinite) && values.some((value) => value !== 0), 'Invalid saved query vector')
      return values
    },
  }
}

interface JourneyState {
  session: JourneySession
  attempted_calls: number
  delivered_code_points: number
  delivered_bytes: number
  semantic_calls: number
  exhausted: boolean
  tail: Promise<unknown>
}
export interface JourneyRecord { [key: string]: unknown }

/** Tests may inject a forwarder; CLI always uses current production handlers. */
export function createJourneyAdapter(options: {
  sessions: JourneySession[]
  forward: (request: Request, session: JourneySession) => Promise<Response>
  record: (session: JourneySession, record: JourneyRecord) => void
  limits?: { calls: number, code_points: number }
  searchKDefault?: number
}) {
  const limits = options.limits ?? JOURNEY_LIMITS
  const searchKDefault = options.searchKDefault ?? 8
  assert(Number.isSafeInteger(searchKDefault) && searchKDefault >= 1 && searchKDefault <= 8)
  assert(limits.calls > 0 && limits.code_points >= EXHAUSTED.length)
  const states = new Map(options.sessions.map((session) => [session.id, {
    session, attempted_calls: 0, delivered_code_points: 0, delivered_bytes: 0,
    semantic_calls: 0, exhausted: false, tail: Promise.resolve(),
  } satisfies JourneyState]))
  const totals = (state: JourneyState) => ({ attempted_calls: state.attempted_calls,
    delivered_code_points: state.delivered_code_points, delivered_bytes: state.delivered_bytes,
    semantic_calls: state.semantic_calls, exhausted: state.exhausted })

  async function dispatch(request: Request, state: JourneyState, path: string, wire: string) {
    const url = new URL(request.url)
    if (REST_FIELDS[path]) {
      if (request.method !== 'GET' || wire) return error('invalid_method_or_body', 405)
      const keys = [...url.searchParams.keys()]
      if (new Set(keys).size !== keys.length || keys.some((key) => !REST_FIELDS[path].includes(key))) {
        return error('unknown_or_duplicate_parameter')
      }
      if (path === '/v1/search') {
        if (url.searchParams.get('q') !== state.session.question) return error('frozen_query_required')
        if (state.semantic_calls) return error('semantic_call_already_used')
        if (state.attempted_calls !== 1) return error('initial_semantic_call_required')
        state.semantic_calls++
        if (!url.searchParams.has('k')) url.searchParams.set('k', String(searchKDefault))
      } else if (!state.semantic_calls) return error('initial_semantic_call_required')
      return options.forward(new Request('http://localhost' + path + url.search), state.session)
    }
    if (path === '/mcp') {
      if (request.method !== 'POST' || url.search) return error('invalid_method_or_query', 405)
      let rpc: any
      try { rpc = JSON.parse(wire) } catch { return error('invalid_json') }
      if (!object(rpc) || !onlyKeys(rpc, ['jsonrpc', 'id', 'method', 'params'])
          || rpc.jsonrpc !== '2.0' || rpc.method !== 'tools/call'
          || !['number', 'string'].includes(typeof rpc.id) || !object(rpc.params)
          || !onlyKeys(rpc.params, ['name', 'arguments'])) return error('invalid_mcp_envelope')
      const name = rpc.params.name
      const args = rpc.params.arguments
      if (typeof name !== 'string' || !MCP_FIELDS[name] || !object(args)
          || !onlyKeys(args, MCP_FIELDS[name])) return error('unsupported_mcp_tool_or_fields')
      if (name === 'search') {
        if (args.query !== state.session.question) return error('frozen_query_required')
        if (state.semantic_calls) return error('semantic_call_already_used')
        if (state.attempted_calls !== 1) return error('initial_semantic_call_required')
        state.semantic_calls++
      } else if (!state.semantic_calls) return error('initial_semantic_call_required')
      return options.forward(new Request('http://localhost/mcp', { method: 'POST',
        headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream',
          'mcp-protocol-version': '2025-06-18' }, body: wire }), state.session)
    }
    return error('endpoint_not_allowed', 404)
  }

  async function perform(request: Request, state: JourneyState, path: string) {
    const started = performance.now()
    const requestBody = await request.text()
    const setup = path === '/setup' && request.method === 'GET' && !new URL(request.url).search && !requestBody
    if (!setup) state.attempted_calls++
    const call = state.attempted_calls
    options.record(state.session, { event: 'request', at: new Date().toISOString(), call,
      setup_excluded: setup, request: { method: request.method, url: request.url,
        headers: Object.fromEntries(request.headers), body: requestBody } })
    let result: Response
    if (setup) {
      result = json({ question_id: state.session.question_id, question: state.session.question,
        budgets: limits, usage: totals(state), setup_excluded_from_budget: true,
        instructions: 'Make the exact question your first API call via semantic search. One semantic call only. '
          + 'All API attempts count; all complete response bodies count, including repeated text and JSON. '
          + 'Prefix every returned /v1/ link with this session base. No external sources.',
        rest: { method: 'GET', endpoints: REST_FIELDS, search_k_default: searchKDefault,
          content_length_default: 6000, content_length_max: 32000,
          literal_find: 'q is a literal case-insensitive string within one paper' },
        mcp: { method: 'POST', path: '/mcp', tools: MCP_FIELDS,
          envelope: { jsonrpc: '2.0', id: 1, method: 'tools/call',
            params: { name: 'search', arguments: { query: state.session.question } } } } })
    } else if (state.exhausted || call > limits.calls) {
      state.exhausted = true
      result = error('budget_exhausted', 429)
    } else {
      try { result = await dispatch(request, state, path, requestBody) }
      catch { result = error('adapter_request_failed', 503) }
    }
    let body = await result.text()
    const upstream = { status: result.status, headers: Object.fromEntries(result.headers), body }
    let suppressed = false
    if (!setup) {
      // Reserve one complete terminal error. Subsequent exhausted responses have
      // an explicit error header and empty body so they cannot exceed the cap.
      if (!state.exhausted && state.delivered_code_points + pointLength(body)
          > limits.code_points - pointLength(EXHAUSTED)) {
        state.exhausted = true
        suppressed = true
      }
      if (state.exhausted) {
        body = state.delivered_code_points + pointLength(EXHAUSTED) <= limits.code_points ? EXHAUSTED : ''
        result = new Response(null, { status: 429, headers: { 'content-type': 'application/json; charset=utf-8',
          'cache-control': 'no-store', 'x-journey-error': 'budget_exhausted' } })
      }
      state.delivered_code_points += pointLength(body)
      state.delivered_bytes += Buffer.byteLength(body, 'utf8')
    }
    const headers = new Headers(result.headers)
    headers.set('x-journey-attempted-calls', String(state.attempted_calls))
    headers.set('x-journey-delivered-code-points', String(state.delivered_code_points))
    headers.set('x-journey-delivered-bytes', String(state.delivered_bytes))
    headers.delete('content-length')
    options.record(state.session, { event: 'response', at: new Date().toISOString(), call,
      setup_excluded: setup, elapsed_ms: performance.now() - started,
      response: { status: result.status, headers: Object.fromEntries(headers), body },
      response_code_points: pointLength(body), response_bytes: Buffer.byteLength(body, 'utf8'),
      upstream_suppressed_for_budget: suppressed, ...(suppressed ? { upstream } : {}), ...totals(state) })
    return new Response(body, { status: result.status, headers })
  }

  return {
    async fetch(request: Request) {
      const url = new URL(request.url)
      if (!['localhost', '127.0.0.1'].includes(url.hostname)) return error('loopback_only', 403)
      const match = /^\/session\/([A-Za-z0-9_-]+)(\/.*)$/.exec(url.pathname)
      const state = match ? states.get(match[1]) : undefined
      if (!state) return error('unknown_session', 404)
      // Serial execution prevents concurrent calls bypassing either allowance.
      const pending = state.tail.then(() => perform(request, state, match![2]))
      state.tail = pending.catch(() => undefined)
      return pending
    },
  }
}

async function filesystemAssets(directory: string) {
  const root = await realpath(directory)
  return { async fetch(request: Request) {
    const url = new URL(request.url)
    assert(url.origin === 'https://full-probe-assets.invalid' && request.method === 'GET')
    const path = decodeURIComponent(url.pathname.slice(1))
    assert(path && !isAbsolute(path) && !path.includes('\\')
      && path.split('/').every((part) => part && part !== '.' && part !== '..'), 'Unsafe asset path')
    const full = await realpath(resolve(root, path))
    const rel = relative(root, full)
    assert(rel !== '..' && !rel.startsWith('..' + sep) && !isAbsolute(rel), 'Asset escaped root')
    const info = await stat(full)
    assert(info.isFile())
    return new Response(Readable.toWeb(createReadStream(full)) as ReadableStream<Uint8Array>,
      { headers: { 'content-length': String(info.size) } })
  } }
}

export async function runJourneyServer(options: {
  assets: string, manifestSha: string, queryVectors: string, queryMetadata: string,
  sessions: string, out: string, port: number, wasm: string, vocab: string,
}): Promise<Server> {
  const manifestBytes = readFileSync(resolve(options.assets, 'probe.json'))
  assert(hash(manifestBytes) === options.manifestSha, 'Pinned manifest mismatch')
  const manifest = JSON.parse(manifestBytes.toString('utf8'))
  assert(manifest.passage_count === 40575 && manifest.synthetic === false, 'Expected full 40575-passage real runtime')
  const queryBytes = readFileSync(options.queryVectors)
  const queryMetadata = JSON.parse(readFileSync(options.queryMetadata, 'utf8'))
  const bank = readQueryBank(queryBytes, queryMetadata, manifest)
  const sessions = parseSessions(JSON.parse(readFileSync(options.sessions, 'utf8')), bank.count)
  for (const session of sessions) bank.vector(session.vector_row)
  const currentSession = new AsyncLocalStorage<JourneySession>()
  const assets = await filesystemAssets(options.assets)
  const load = createFullCorpusStoreLoader(assets, options.manifestSha, async (input) => {
    const session = currentSession.getStore()
    assert(session && input === embed.query_template + session.question, 'Unregistered semantic query has no vector')
    return bank.vector(session.vector_row)
  }, async () => true, { module: new WebAssembly.Module(readFileSync(options.wasm)) })
  const bundle = await load()
  const service = createService(bundle.store, new WordPieceTokenizer(readFileSync(options.vocab, 'utf8')))
  const handler = createBoundedProbeHandler(async () => service)
  mkdirSync(options.out, { recursive: true })
  // Never silently append a second run to the same evaluation output.
  writeFileSync(resolve(options.out, 'run.json'), JSON.stringify({ schema_version: 1,
    created_at: new Date().toISOString(), runtime: process.version, scope: 'local-real-agent-journey',
    manifest_sha256: options.manifestSha, release_id: manifest.release_id, passage_count: manifest.passage_count,
    query_vectors_sha256: hash(queryBytes), query_manifest_sha256: queryMetadata.query_manifest_sha256,
    query_template: embed.query_template, limits: JOURNEY_LIMITS,
    counting: 'Entire UTF-8 response body decoded into Unicode code points, including JSON, snippets, repeated text and errors. Setup excluded. One terminal error reserved.',
    sessions: sessions.map(({ id, question_id, question, vector_row }) => ({ id, question_id, question, vector_row })),
  }, null, 2) + '\n', { flag: 'wx' })
  const adapter = createJourneyAdapter({ sessions,
    forward: (request, session) => currentSession.run(session, () => handler.fetch(request)),
    record: (session, record) => appendFileSync(resolve(options.out, session.id + '.jsonl'), JSON.stringify(record) + '\n'),
  })
  const server = createServer(async (req, res) => {
    try {
      const remote = req.socket.remoteAddress
      if (remote !== '127.0.0.1' && remote !== '::ffff:127.0.0.1') {
        res.writeHead(403).end(); return
      }
      const host = req.headers.host
      if (host !== `127.0.0.1:${options.port}` && host !== `localhost:${options.port}`) {
        res.writeHead(403).end(); return
      }
      const chunks: Buffer[] = []
      let length = 0
      for await (const part of req) {
        length += part.length
        if (length > 16384) { res.writeHead(413).end(); return }
        chunks.push(part)
      }
      const method = req.method ?? 'GET'
      const request = new Request(`http://127.0.0.1:${options.port}${req.url}`, { method,
        headers: Object.fromEntries(Object.entries(req.headers).filter((row) => typeof row[1] === 'string')) as Record<string, string>,
        ...(['GET', 'HEAD'].includes(method) ? {} : { body: Buffer.concat(chunks) }) })
      const response = await adapter.fetch(request)
      res.writeHead(response.status, Object.fromEntries(response.headers))
      res.end(await response.text())
    } catch { res.writeHead(500, { 'content-type': 'application/json' }).end('{"error":{"code":"adapter_failed"}}') }
  })
  server.requestTimeout = 30000
  await new Promise<void>((resolveReady, reject) => {
    server.once('error', reject)
    server.listen(options.port, '127.0.0.1', () => { server.removeListener('error', reject); resolveReady() })
  })
  process.stdout.write(JSON.stringify({ ready: true, origin: `http://127.0.0.1:${options.port}`,
    sessions: sessions.length, passages: manifest.passage_count, output: options.out }) + '\n')
  return server
}

function parseOptions(argv: string[]) {
  const args = new Map<string, string>()
  const allowed = ['--assets', '--manifest-sha', '--query-vectors', '--query-metadata', '--sessions', '--out', '--port', '--wasm', '--vocab']
  for (let i = 0; i < argv.length; i += 2) {
    assert(allowed.includes(argv[i]) && argv[i + 1] && !args.has(argv[i]), 'Invalid CLI argument')
    args.set(argv[i], argv[i + 1])
  }
  for (const flag of allowed.slice(0, 7)) assert(args.has(flag), 'Missing ' + flag)
  const port = Number(args.get('--port'))
  assert(Number.isSafeInteger(port) && port > 0 && port <= 65535, 'Invalid port')
  return { assets: resolve(args.get('--assets')!), manifestSha: args.get('--manifest-sha')!,
    queryVectors: resolve(args.get('--query-vectors')!), queryMetadata: resolve(args.get('--query-metadata')!),
    sessions: resolve(args.get('--sessions')!), out: resolve(args.get('--out')!), port,
    wasm: resolve(args.get('--wasm') ?? 'probe-kernel/scan.wasm'),
    vocab: resolve(args.get('--vocab') ?? 'tokenizer/vocab.txt') }
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href
    && !process.argv.includes('--retained-reading')) {
  await runJourneyServer(parseOptions(process.argv.slice(2)))
}
