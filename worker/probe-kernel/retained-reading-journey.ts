/** Replay two exact live search bodies, then measure local reading/catalog recovery.
 * No model, query-vector bank, provider calls or further semantic searches.
 * CLI accepts the existing run_agent_journey_session.py launcher's arguments.
 */
import assert from 'node:assert/strict'
import { createHash } from 'node:crypto'
import { appendFileSync, mkdirSync, readFileSync, realpathSync, writeFileSync } from 'node:fs'
import { createServer } from 'node:http'
import { resolve, sep } from 'node:path'
import { pathToFileURL } from 'node:url'
import { gunzipSync } from 'node:zlib'
import { createJourneyAdapter, JOURNEY_LIMITS } from './agent-journey'
import { createFullCorpusStoreLoader } from '../src/full-corpus-store'
import { createBoundedProbeHandler } from '../src/probe-admission'
import { createService } from '../src/service'
import { WordPieceTokenizer } from '../src/tokenize'

export const EVIDENCE_SHA = '715ccbe7ee7e3d9f3dc51a33a451ea7cd583957298b5ae6314d9036928d58b78'
export const REPORT_SHA = '89b4a5fe6cda64396e4e485a189496928417eda3569d60fccaaf2677d5b58b2a'
export const MANIFEST_SHA = '6b9c87883f525a128eb9a48aead5914d9524ba2f7433ff3b14c62b3c0d970b47'
const sha = (value: Uint8Array | string) => createHash('sha256').update(value).digest('hex')

export function readSeeds(bytes: Uint8Array) {
  assert(sha(bytes) === EVIDENCE_SHA, 'Committed evidence checksum mismatch')
  const evidence = JSON.parse(gunzipSync(bytes).toString('utf8'))
  assert(evidence.workflow_run_id === 40806851930 && evidence.artifact_id === 12868622798)
  assert(sha(evidence.original_run_report_utf8) === REPORT_SHA, 'Original report checksum mismatch')
  const report = JSON.parse(evidence.original_run_report_utf8)
  assert(report.smoke_gate === 'passed' && report.packed_manifest_sha256 === MANIFEST_SHA)
  const seeds = report.requests.filter((row: any) => row.kind === 'new_query')
  assert(seeds.length === 2 && report.journeys.length === 2)
  return seeds.map((row: any, index: number) => {
    const url = new URL(row.path, 'http://localhost')
    assert(row.method === 'GET' && row.status === 200 && row.success === true)
    assert(url.pathname === '/v1/search' && url.searchParams.get('k') === '3')
    const question = url.searchParams.get('q')!
    assert(question === report.journeys[index].query && JSON.parse(row.response_text).hits.length === 3)
    return { id: `recovery-0${index + 1}`, question_id: `live-smoke-${index + 1}`,
      question, vector_row: -1, response_text: row.response_text as string }
  })
}

export async function run(argv: string[]) {
  assert(argv.filter((value) => value === '--retained-reading').length === 1, 'Explicit replay mode required')
  argv = argv.filter((value) => value !== '--retained-reading')
  assert(argv.length % 2 === 0)
  const args = new Map<string, string>()
  const allowed = ['--assets', '--manifest-sha', '--query-vectors', '--query-metadata', '--sessions', '--out', '--port']
  for (let i = 0; i < argv.length; i += 2) {
    assert(allowed.includes(argv[i]) && argv[i + 1] && !args.has(argv[i]), 'Invalid argument')
    args.set(argv[i], argv[i + 1])
  }
  for (const key of allowed) assert(args.has(key), 'Missing ' + key)
  assert(args.get('--manifest-sha') === MANIFEST_SHA)
  const assets = realpathSync(args.get('--assets')!)
  const raw = readFileSync(resolve(assets, 'probe.json'))
  assert(sha(raw) === MANIFEST_SHA, 'Runtime manifest mismatch')
  const manifest = JSON.parse(raw.toString('utf8'))
  assert(manifest.passage_count === 40575 && manifest.synthetic === false)
  const seeds = readSeeds(readFileSync('probe-results/retained-smoke-40806851930.evidence.json.gz'))
  const sessions = seeds.map(({ response_text, ...session }: any) => session)
  assert.deepEqual(JSON.parse(readFileSync(args.get('--sessions')!, 'utf8')),
    { sessions: sessions.map(({ vector_row, ...session }: any) => session) }, 'Session/question pairing differs')
  const load = createFullCorpusStoreLoader({ async fetch(request: Request) {
    const url = new URL(request.url)
    assert(url.origin === 'https://full-probe-assets.invalid' && request.method === 'GET')
    const file = realpathSync(resolve(assets, decodeURIComponent(url.pathname.slice(1))))
    assert(file.startsWith(assets + sep), 'Asset escaped root')
    const bytes = readFileSync(file)
    return new Response(bytes, { headers: { 'content-length': String(bytes.length) } })
  } }, MANIFEST_SHA, async () => { throw new Error('No query encoder; semantic calls cannot execute') },
  async () => false, { module: new WebAssembly.Module(readFileSync('probe-kernel/scan.wasm')) })
  const bundle = await load()
  const service = createService(bundle.store, new WordPieceTokenizer(readFileSync('tokenizer/vocab.txt', 'utf8')))
  const handler = createBoundedProbeHandler(async () => service)
  const out = resolve(args.get('--out')!)
  mkdirSync(out, { recursive: true })
  writeFileSync(resolve(out, 'run.json'), JSON.stringify({ schema_version: 1,
    scope: 'local-reading-recovery-after-replayed-live-search', source_run: 40806851930,
    evidence_commit: '7d928317d808a37cd87e00577855567464f8866b', seed_runtime_commit: '02c18b933dfc64dcbcdbb9f129815c8ca37ed20b',
    evidence_sha256: EVIDENCE_SHA, report_sha256: REPORT_SHA, manifest_sha256: MANIFEST_SHA,
    provider_calls: 0, query_vectors_loaded: false, semantic_reformulation_executed: false,
    seed_k: 3, limits: JOURNEY_LIMITS, sessions }, null, 2) + '\n', { flag: 'wx' })
  const adapter = createJourneyAdapter({ sessions, searchKDefault: 3,
    forward: async (request, session) => {
      const url = new URL(request.url)
      assert(url.pathname !== '/mcp', 'REST recovery only')
      if (url.pathname !== '/v1/search') return handler.fetch(request)
      assert(url.searchParams.get('k') === '3', 'Historical search only returned k=3')
      return new Response(seeds.find((seed: any) => seed.id === session.id)!.response_text,
        { headers: { 'content-type': 'application/json', 'x-journey-source': 'replayed-live-response' } })
    }, record: (session, row) => appendFileSync(resolve(out, session.id + '.jsonl'), JSON.stringify(row) + '\n') })
  const port = Number(args.get('--port'))
  assert(Number.isSafeInteger(port) && port > 0 && port <= 65535)
  const server = createServer(async (req, res) => {
    try {
      assert(['127.0.0.1', '::ffff:127.0.0.1'].includes(req.socket.remoteAddress ?? ''))
      assert([`127.0.0.1:${port}`, `localhost:${port}`].includes(req.headers.host ?? '') && req.method === 'GET')
      const response = await adapter.fetch(new Request(`http://127.0.0.1:${port}${req.url}`))
      res.writeHead(response.status, Object.fromEntries(response.headers)).end(await response.text())
    } catch { res.writeHead(400).end('{"error":{"code":"invalid_recovery_request"}}') }
  })
  server.requestTimeout = 30000
  await new Promise<void>((ok, fail) => { server.once('error', fail); server.listen(port, '127.0.0.1', ok) })
  process.stdout.write(JSON.stringify({ ready: true, scope: 'reading-recovery', sessions: 2, output: out }) + '\n')
  return server
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) await run(process.argv.slice(2))
