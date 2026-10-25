/** Local full-corpus memory and contract harness. No network or Workers AI calls.
 *
 * Build from worker/: npx esbuild probe-kernel/full-memory.ts --bundle \
 *   --platform=node --format=esm --outfile=/tmp/full-memory.mjs
 * Run: node --expose-gc /tmp/full-memory.mjs --assets ../agent_full_runtime \
 *   --manifest-sha SHA256 --wasm probe-kernel/scan.wasm \
 *   --vocab tokenizer/vocab.txt --out /tmp/full-memory.json \
 *   --data-label geometry-fixture --canonical ../agent_full_probe/probe.json
 *
 * heapUsed + external is a Node estimate, not Cloudflare isolate accounting.
 * arrayBuffers is a subset of external and must NOT be added a second time.
 * Timers cannot interrupt synchronous work. Observed peaks are lower bounds;
 * forced-GC snapshots measure retained memory only, between workload phases.
 */
import assert from 'node:assert/strict'
import { createHash } from 'node:crypto'
import { createReadStream, readFileSync } from 'node:fs'
import { mkdir, realpath, stat, writeFile } from 'node:fs/promises'
import { Session } from 'node:inspector'
import { cpus } from 'node:os'
import { dirname, isAbsolute, relative, resolve, sep } from 'node:path'
import { performance } from 'node:perf_hooks'
import { Readable } from 'node:stream'
import { setImmediate as immediate } from 'node:timers/promises'
import { pathToFileURL } from 'node:url'
import type { GraphDoc, NodeCard } from '../src/corpus'
import { createFullCorpusStore, createFullCorpusStoreLoader, createGeometryFixtureStoreLoader } from '../src/full-corpus-store'
import { BoundedAdmission, createBoundedProbeHandler, PROBE_REQUEST_LIMITS } from '../src/probe-admission'
import { CONTENT_MAX, createService } from '../src/service'
import { embed, pointLength, WordPieceTokenizer } from '../src/tokenize'

const MIB = 1024 * 1024
const DEFAULT_THRESHOLD = 96 * MIB
const RETAINED_GROWTH_ALLOWANCE = 8 * MIB
const SAMPLE_INTERVAL_MS = 5
const SEARCH_ROUND_SIZE = 80

export interface MemorySample {
  phase: string
  event: string
  elapsed_ms: number
  heap_used: number
  heap_total: number
  external: number
  array_buffers: number
  rss: number
  heap_plus_external: number
  heap_plus_array_buffers: number
  resident_index_bytes?: number
  current_asset_bytes?: number
}

export function readMemory(phase: string, event: string, started: number): MemorySample {
  const usage = process.memoryUsage()
  return {
    phase, event, elapsed_ms: performance.now() - started,
    heap_used: usage.heapUsed, heap_total: usage.heapTotal,
    external: usage.external, array_buffers: usage.arrayBuffers, rss: usage.rss,
    heap_plus_external: usage.heapUsed + usage.external,
    heap_plus_array_buffers: usage.heapUsed + usage.arrayBuffers,
  }
}

export function summarizeSamples(samples: MemorySample[]) {
  assert(samples.length, 'Memory sampling produced no observations')
  const keys = ['heap_used', 'heap_total', 'external', 'array_buffers', 'rss',
    'heap_plus_external', 'heap_plus_array_buffers'] as const
  const peaks = Object.fromEntries(keys.map((key) => [key, Math.max(...samples.map((row) => row[key]))]))
  const peak = samples.reduce((best, row) => row.heap_plus_external > best.heap_plus_external ? row : best)
  return { samples: samples.length, peaks, observed_peak: peak }
}

/** Use a streamed file body, not a preloaded filesystem fixture map. */
export async function filesystemAssets(directory: string, sample: (event: string) => void) {
  const root = await realpath(directory)
  const counts = new Map<string, number>()
  let inFlight = 0
  let maxInFlight = 0
  let bytesRead = 0
  return {
    counts,
    stats: () => ({ reads: [...counts.values()].reduce((a, b) => a + b, 0),
      distinct_assets: counts.size, bytes_read: bytesRead,
      active_streams: inFlight, max_concurrent_streams: maxInFlight }),
    async fetch(request: Request): Promise<Response> {
      const url = new URL(request.url)
      assert.equal(url.origin, 'https://full-probe-assets.invalid')
      assert.equal(request.method, 'GET')
      const path = decodeURIComponent(url.pathname.slice(1))
      assert(path && !isAbsolute(path) && !path.includes('\\')
        && path.split('/').every((part) => part && part !== '.' && part !== '..'), 'Unsafe asset path')
      const fullPath = await realpath(resolve(root, path))
      const rel = relative(root, fullPath)
      assert(rel !== '..' && !rel.startsWith('..' + sep) && !isAbsolute(rel), 'Asset escaped fixture directory')
      const info = await stat(fullPath)
      assert(info.isFile())
      counts.set(path, (counts.get(path) ?? 0) + 1)
      inFlight++
      maxInFlight = Math.max(maxInFlight, inFlight)
      sample('asset-open:' + path)
      const file = createReadStream(fullPath, { highWaterMark: 64 * 1024 })
      file.once('close', () => { inFlight--; sample('asset-close:' + path) })
      file.on('data', (chunk) => { bytesRead += chunk.length })
      const body = Readable.toWeb(file) as ReadableStream<Uint8Array>
      return new Response(body, { headers: { 'content-length': String(info.size) } })
    },
  }
}

interface Options {
  assets: string
  manifestSha: string
  wasm: string
  vocab: string
  out: string
  dataLabel: 'real-embeddings' | 'geometry-fixture'
  canonical: string
  expectedPassages?: number
  threshold: number
}

function parseOptions(argv: string[]): Options {
  const args = new Map<string, string>()
  const allowed = new Set(['--assets', '--manifest-sha', '--wasm', '--vocab', '--out',
    '--data-label', '--expected-passages', '--threshold-mib', '--canonical'])
  for (let index = 0; index < argv.length; index += 2) {
    assert(allowed.has(argv[index]) && argv[index + 1] && !args.has(argv[index]), 'Unknown or incomplete argument')
    args.set(argv[index], argv[index + 1])
  }
  for (const required of ['--assets', '--manifest-sha', '--wasm', '--vocab', '--out', '--data-label', '--canonical']) {
    assert(args.has(required), 'Required argument: ' + required)
  }
  assert(/^[a-f0-9]{64}$/.test(args.get('--manifest-sha')!), 'Manifest SHA must be 64 lowercase hex characters')
  const dataLabel = args.get('--data-label')
  assert(dataLabel === 'real-embeddings' || dataLabel === 'geometry-fixture', 'Explicit data provenance label required')
  const threshold = Number(args.get('--threshold-mib') ?? 96) * MIB
  assert(Number.isFinite(threshold) && threshold > 0 && threshold <= 128 * MIB, 'Threshold must be in (0,128] MiB')
  const expectedPassages = args.has('--expected-passages') ? Number(args.get('--expected-passages')) : undefined
  assert(expectedPassages === undefined || (Number.isSafeInteger(expectedPassages) && expectedPassages > 0))
  return { assets: resolve(args.get('--assets')!), manifestSha: args.get('--manifest-sha')!,
    wasm: resolve(args.get('--wasm')!), vocab: resolve(args.get('--vocab')!),
    out: resolve(args.get('--out')!), canonical: resolve(args.get('--canonical')!), dataLabel, expectedPassages, threshold }
}

async function retainedSample(phase: string, started: number) {
  const gc = (globalThis as { gc?: () => void }).gc
  assert(gc, 'Run with node --expose-gc; retained snapshots require explicit GC')
  // Two collections separated by a turn let completed streams/promise frames go.
  await immediate()
  gc()
  await immediate()
  gc()
  return readMemory(phase, 'retained-after-forced-gc', started)
}

async function inspectorUsage() {
  const session = new Session()
  session.connect()
  try {
    return await new Promise<Record<string, number>>((resolveResult, reject) => {
      session.post('Runtime.getHeapUsage', (error, value) => error ? reject(error) : resolveResult(value))
    })
  } finally { session.disconnect() }
}

function checkContent(result: Awaited<ReturnType<ReturnType<typeof createService>['content']>>, node: NodeCard) {
  assert.equal(result.paper_id, node.id)
  assert.equal(result.available, true)
  assert.equal(result.total_length, node.text.code_points)
  assert(pointLength(result.text) <= CONTENT_MAX)
  assert.equal(pointLength(result.text), Math.min(CONTENT_MAX, result.total_length - result.offset))
  assert.equal(result.next_offset,
    result.offset + pointLength(result.text) < result.total_length ? result.offset + pointLength(result.text) : null)
}

function canonicalIdentity(path: string) {
  const bytes = readFileSync(path)
  const value = JSON.parse(bytes.toString('utf8'))
  assert.equal(value.kind, 'full-corpus')
  assert.equal(value.synthetic, false)
  return { sha256: createHash('sha256').update(bytes).digest('hex'),
    passage_count: value.passage_count, paper_ids: value.paper_ids,
    text_paper_ids: value.text_paper_ids, rows_sha256: value.rows_sha256 }
}

const SOURCE_FILES = [
  'worker/probe-kernel/full-memory.ts', 'worker/src/full-corpus-store.ts',
  'worker/src/full-search-index.ts', 'worker/src/static-search-int8.ts',
  'worker/src/probe-admission.ts', 'worker/src/service.ts', 'worker/src/corpus.ts',
  'worker/src/http.ts', 'worker/src/mcp.ts', 'worker/src/contracts.ts',
  'worker/src/tokenize.ts', 'worker/src/signatures.ts', 'worker/embed.json',
  'worker/probe-kernel/scan.wasm', 'src/pack_full_search_probe.py',
]

function sourceHashes(repo: string) {
  return Object.fromEntries(SOURCE_FILES.map((path) => [path,
    createHash('sha256').update(readFileSync(resolve(repo, path))).digest('hex')]))
}

/** MCP transports may return JSON or a bounded SSE message. Check the actual wire. */
export function parseMcpWire(wire: string) {
  if (!wire.startsWith('event:') && !wire.startsWith('data:')) return JSON.parse(wire)
  const messages = wire.split('\n\n').flatMap((frame) => {
    const data = frame.split('\n').filter((line) => line.startsWith('data:')).map((line) => line.slice(5).trim()).join('\n')
    return data ? [JSON.parse(data)] : []
  })
  assert.equal(messages.length, 1, 'Expected one bounded MCP message')
  return messages[0]
}

export async function runMemoryHarness(options: Options) {
  // Input verification is not a deployed request. Release the large canonical
  // manifest before measuring the compact runtime loader.
  const canonical = canonicalIdentity(options.canonical)
  const repo = resolve(dirname(options.vocab), '../..')
  const sources = sourceHashes(repo)
  const started = performance.now()
  const samples: MemorySample[] = []
  const phases: Record<string, unknown>[] = []
  const retained = new Map<string, MemorySample>()
  let phase = 'baseline'
  let sampleCount = 0
  let timerPeak: MemorySample | undefined
  let phasePeak: MemorySample | undefined
  const sample = (event: string, extra?: { resident_index_bytes: number, current_asset_bytes: number }) => {
    const row = { ...readMemory(phase, event, started), ...extra }
    sampleCount++
    if (!phasePeak || row.heap_plus_external > phasePeak.heap_plus_external) phasePeak = row
    if (event === 'timer') {
      if (!timerPeak || row.heap_plus_external > timerPeak.heap_plus_external) timerPeak = row
    } else {
      // At most 8192 retained observations; preserve maxima even if a longer
      // churn run hits this observer cap. No unbounded diagnostic allocation.
      if (samples.length < 8192) samples.push(row)
    }
  }
  const baseline = await retainedSample(phase, started)
  samples.push(baseline)
  retained.set(phase, baseline)
  const assets = await filesystemAssets(options.assets, (event) => sample(event))
  let timer: ReturnType<typeof setInterval> | undefined
  const runPhase = async (name: string, operation: () => Promise<Record<string, unknown> | void>) => {
    assert(performance.now() - started < 240_000, 'Local workload exceeded four-minute budget')
    phase = name
    timerPeak = undefined
    phasePeak = undefined
    const from = samples.length
    sample('phase-start')
    const before = performance.now()
    timer = setInterval(() => sample('timer'), SAMPLE_INTERVAL_MS)
    try {
      const details = await operation()
      sample('phase-completed-before-gc')
      clearInterval(timer)
      timer = undefined
      if (timerPeak) samples.push(timerPeak)
      if (phasePeak) samples.push(phasePeak)
      const after = await retainedSample(name, started)
      samples.push(after)
      retained.set(name, after)
      phases.push({ name, wall_ms: performance.now() - before, ...details,
        ...summarizeSamples(samples.slice(from)), retained: after, assets: assets.stats() })
      process.stderr.write(name + ': retained ' + (after.heap_plus_external / MIB).toFixed(2) + ' MiB\n')
    } finally {
      if (timer) clearInterval(timer)
      timer = undefined
    }
  }

  let bundle: Awaited<ReturnType<typeof createFullCorpusStore>>
  let service: ReturnType<typeof createService> | undefined
  let handler: ReturnType<typeof createBoundedProbeHandler>
  let graph: GraphDoc
  let orderedPapers: NodeCard[]
  let embeddedQueries = 0
  let serviceConstructions = 0
  let loadCalls = 0
  let contractRequests = 0
  let productionRejectedFixture = false
  let coldOverload = 0
  let sustainedOverload = 0
  const embeddings = new BoundedAdmission(2, 2, 2000)
  const queryVectors: number[][] = []
  const referenceRows: { sample_index: number, packed_index: number, source_index: number, paper_id: string }[] = []
  const limits = PROBE_REQUEST_LIMITS
  const report: Record<string, unknown> = {
    schema_version: 2, gate: options.dataLabel === 'geometry-fixture' ? 'geometry-memory' : 'full-real-memory',
    scope: 'local-node-full-corpus-memory-contracts',
    data_label: options.dataLabel, production_readiness: 'unverified',
    cloudflare_memory_gate: 'unverified', semantic_quality_gate: 'not-measured',
    workers_ai_compatibility: 'not-measured', manifest_sha256: options.manifestSha,
    packed_manifest_path: resolve(options.assets, 'probe.json'), source_sha256: sources,
    executed_bundle_sha256: createHash('sha256').update(readFileSync(process.argv[1])).digest('hex'),
    runtime: { node: process.version, v8: process.versions.v8, platform: process.platform,
      arch: process.arch, cpu: cpus()[0]?.model },
    method: {
      local_threshold_bytes: options.threshold, default_threshold_bytes: DEFAULT_THRESHOLD,
      aggregate: 'heapUsed + external; arrayBuffers is already included in external',
      rss: 'Whole Node process RSS, diagnostic only; not Cloudflare isolate memory',
      peak: 'Observed lower bound from phase, loader and 5 ms timer checkpoints; synchronous allocation peaks may be missed',
      retained: 'Explicit GC only between phases; never forced inside a workload',
      assets: 'Streamed local filesystem; Node HTTP/stream allocation differs from Cloudflare Static Assets',
      queries: 'Stored FP32 reference vectors with distinct synthetic labels; no natural-language embedding or quality claim',
      observer: 'No heap snapshots during workload; at most 8192 ordinary samples plus phase maxima',
      sources: ['https://nodejs.org/api/process.html#processmemoryusage',
        'https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-getHeapUsage',
        'https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/'],
    },
  }
  const wireRequest = async (request: Request, allowOverload = false) => {
    const response = await handler.fetch(request)
    const wire = await response.text()
    contractRequests++
    sample('serialized-response-live')
    if (allowOverload && response.status === 503) {
      assert.equal(JSON.parse(wire).error.code, 'probe_overloaded')
      return null
    }
    assert.equal(response.status, 200, wire.slice(0, 500))
    return new URL(request.url).pathname === '/mcp' ? parseMcpWire(wire) : JSON.parse(wire)
  }
  const rest = (path: string, args: Record<string, string | number>) => wireRequest(new Request(
    'http://localhost' + path + '?' + new URLSearchParams(Object.entries(args).map(([key, value]) => [key, String(value)])),
  ))
  let rpcId = 0
  const mcpRequest = (name: string, args: Record<string, unknown>) => new Request('http://localhost/mcp', {
    method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream' },
    body: JSON.stringify({ jsonrpc: '2.0', id: ++rpcId, method: 'tools/call', params: { name, arguments: args } }),
  })
  const mcp = async (name: string, args: Record<string, unknown>) => {
    const envelope = await wireRequest(mcpRequest(name, args))
    assert.equal(envelope.result?.isError ?? false, false, JSON.stringify(envelope).slice(0, 500))
    const result = envelope.result.structuredContent
    assert.deepEqual(JSON.parse(envelope.result.content[0].text), result)
    return result
  }
  try {
    await runPhase('initialize-concurrent-cold-burst', async () => {
      const module = new WebAssembly.Module(readFileSync(options.wasm))
      const loaderFactory = options.dataLabel === 'geometry-fixture'
        ? createGeometryFixtureStoreLoader : createFullCorpusStoreLoader
      const load = loaderFactory(assets, options.manifestSha, async (input) => embeddings.run(async () => {
        const match = /memory workload query (\d+)/.exec(input)
        assert(match && queryVectors.length, 'Unexpected live embedding request')
        embeddedQueries++
        // One turn exposes actual concurrency/queue bounds without any provider.
        await immediate()
        return queryVectors[Number(match[1]) % queryVectors.length].slice()
      }), async () => true, { module, memorySample: (value) => sample(value.phase, value) })
      handler = createBoundedProbeHandler(async () => {
        loadCalls++
        bundle = await load()
        if (!service) {
          service = createService(bundle.store, new WordPieceTokenizer(readFileSync(options.vocab, 'utf8')))
          serviceConstructions++
        }
        return service
      })
      const replies = await Promise.all(Array.from({ length: 16 }, () =>
        wireRequest(new Request('http://localhost/v1/catalog?limit=24'), true)))
      coldOverload = replies.filter((reply) => reply === null).length
      assert(coldOverload >= 4, 'Burst above admission+queue limits must be rejected')
      assert(replies.some((reply) => reply !== null), 'No cold request completed')
      assert.equal(serviceConstructions, 1)
      assert.equal(bundle!.manifest.synthetic, options.dataLabel === 'geometry-fixture')
      assert.equal(bundle!.manifest.source_manifest_sha256, canonical.sha256)
      assert.equal(bundle!.manifest.source_rows_sha256, canonical.rows_sha256)
      assert.equal(bundle!.manifest.passage_count, canonical.passage_count)
      assert.deepEqual(bundle!.manifest.paper_ids, canonical.paper_ids)
      assert.deepEqual(bundle!.manifest.text_paper_ids, canonical.text_paper_ids)
      if (options.expectedPassages !== undefined) assert.equal(bundle!.manifest.passage_count, options.expectedPassages)
      graph = await bundle!.store.getJson(bundle!.manifest.graph_path) as GraphDoc
      orderedPapers = Object.values(graph.nodes).filter((node) => node.text.available)
        .sort((a, b) => b.text.code_points - a.text.code_points || a.id.localeCompare(b.id))
      assert(orderedPapers.length >= 5, 'At least five distinct full papers required')
      assert.equal([...assets.counts.keys()].filter((key) => key.includes('/papers/')).length, 0,
        'Initialization eagerly loaded paper documents')
      for (const reply of replies) if (reply) assert.equal(reply.total, bundle!.manifest.paper_ids.length)
      return { passages: bundle!.manifest.passage_count, papers: bundle!.manifest.paper_ids.length,
        text_papers: orderedPapers.length, resident_binary_bytes: bundle!.residentBinaryBytes,
        resident_index_bytes: bundle!.index.residentBytes, eager_paper_loads: 0,
        attempted_requests: 16, rejected_requests: coldOverload, service_constructions: serviceConstructions }
    })
    Object.assign(report, {
      source_manifest_sha256: bundle!.manifest.source_manifest_sha256,
      source_rows_sha256: bundle!.manifest.source_rows_sha256,
      source_embeddings_sha256: bundle!.manifest.source_embeddings?.sha256 ?? null,
      fixture_vectors: bundle!.manifest.fixture_vectors ?? null,
      synthetic: bundle!.manifest.synthetic, release_id: bundle!.manifest.release_id,
      passages: bundle!.manifest.passage_count, papers: bundle!.manifest.paper_ids.length,
    })
    await runPhase('real-loader-rejects-geometry', async () => {
      if (options.dataLabel !== 'geometry-fixture') return { applicable: false }
      const reads = assets.stats().reads
      await assert.rejects(createFullCorpusStore(assets, options.manifestSha,
        async () => { throw Error('No embedding allowed') }),
      (error: { code?: string }) => error.code === 'config_mismatch')
      productionRejectedFixture = true
      assert.equal(assets.stats().reads - reads, 1, 'Real loader must reject fixture before reading index')
      return { production_rejected_fixture: true }
    })
    await runPhase('largest-paper-rest-mcp', async () => {
      const node = orderedPapers![0]
      const content = await rest('/v1/content', { id: node.id, offset: 0, length: CONTENT_MAX })
      checkContent(content, node)
      const tail = await mcp('read_content', { id: node.id,
        offset: Math.max(0, node.text.code_points - CONTENT_MAX), length: CONTENT_MAX })
      checkContent(tail, node)
      const toc = await rest('/v1/contents', { id: node.id })
      assert.equal(toc.total_length, node.text.code_points)
      assert(toc.sections.every((section: { offset: number }) => section.offset >= 0 && section.offset < toc.total_length))
      const found = await mcp('find_in_paper', { id: node.id, q: 'the', offset: 0 })
      assert(found.matches.every((match: { start: number, end: number }) => match.start >= 0 && match.end <= node.text.code_points))
      return { paper_id: node.id, code_points: node.text.code_points,
        content_sha256: createHash('sha256').update(content.text).digest('hex') }
    })
    await runPhase('sustained-admitted-and-rejected-paper-bursts', async () => {
      for (let round = 0; round < 4; round++) {
        const replies = await Promise.all(Array.from({ length: 20 }, (_, index) => {
          const node = orderedPapers![(round * 20 + index + 1) % orderedPapers!.length]
          const request = index % 2 ? mcpRequest('read_content', { id: node.id, offset: 0, length: CONTENT_MAX })
            : new Request('http://localhost/v1/content?' + new URLSearchParams({ id: node.id, offset: '0', length: String(CONTENT_MAX) }))
          return wireRequest(request, true)
        }))
        sustainedOverload += replies.filter((reply) => reply === null).length
        assert(replies.filter((reply) => reply === null).length >= 8)
        assert(replies.some((reply) => reply !== null))
      }
      return { rounds: 4, attempted_requests: 80, rejected_requests: sustainedOverload,
        admission: handler!.admission.stats(), paper_loads: bundle!.paperLoadStats() }
    })
    await runPhase('paper-cache-churn', async () => {
      const nodes = orderedPapers!.slice(0, Math.min(48, orderedPapers!.length))
      for (const node of nodes) checkContent(await rest('/v1/content', { id: node.id, offset: 0, length: CONTENT_MAX }), node)
      return { distinct_papers: nodes.length, configured_cache_entries: embed.limits.paper_cache_entries,
        configured_cache_text_utf8_bytes: embed.limits.paper_cache_bytes,
        cache_accounting_note: 'Production cache bounds text UTF-8 bytes, not complete JS object overhead' }
    })
    await runPhase('prepare-reference-query-vectors', async () => {
      const size = Math.min(16, bundle!.manifest.compatibility.indices.length)
      for (let index = 0; index < size; index++) {
        const sampleIndex = Math.floor(index * (bundle!.manifest.compatibility.indices.length - 1) / (size - 1))
        const reference = await bundle!.referencePassage(sampleIndex)
        queryVectors.push(reference.vector)
        referenceRows.push({ sample_index: sampleIndex, packed_index: bundle!.manifest.compatibility.indices[sampleIndex],
          source_index: reference.row.sourceIndex, paper_id: reference.row.paper_id })
      }
      return { vectors: queryVectors.length, synthetic: bundle!.manifest.synthetic, references: referenceRows }
    })
    const search = async (index: number) => {
      const args = { q: 'memory workload query ' + index, k: 8 }
      const result = index % 2 ? await mcp('search_passages', args) : await rest('/v1/search', args)
      assert.equal(result.corpus_version, bundle!.manifest.release_id)
      assert(result.hits.length > 0 && result.hits.length <= 8)
      assert.equal(new Set(result.hits.map((hit: { paper_id: string }) => hit.paper_id)).size, result.hits.length)
      for (const hit of result.hits) {
        assert(graph!.nodes[hit.paper_id]?.text.available)
        assert(Number.isFinite(hit.score) && hit.start < hit.end)
        assert.equal(hit.corpus_version, bundle!.manifest.release_id)
      }
    }
    for (let round = 0; round < 2; round++) {
      await runPhase('search-cache-churn-' + (round + 1), async () => {
        const before = embeddedQueries
        for (let index = 0; index < SEARCH_ROUND_SIZE; index += 4) {
          await Promise.all([0, 1, 2, 3].map((delta) => search(round * SEARCH_ROUND_SIZE + index + delta)))
        }
        assert.equal(embeddedQueries - before, SEARCH_ROUND_SIZE)
        return { distinct_queries: SEARCH_ROUND_SIZE, request_concurrency: 4,
          embedding_calls: embeddedQueries - before, configured_search_cache_entries: embed.limits.search_cache_entries }
      })
    }
    await runPhase('repeat-cached-queries', async () => {
      const before = embeddedQueries
      for (let repeat = 0; repeat < 4; repeat++) await Promise.all([156, 157, 158, 159].map(search))
      assert.equal(embeddedQueries, before)
      return { requests: 16, embedding_calls: 0 }
    })
    const first = retained.get('search-cache-churn-1')!
    const second = retained.get('search-cache-churn-2')!
    const retainedGrowth = second.heap_plus_external - first.heap_plus_external
    const summary = summarizeSamples(samples)
    const binaryLoads = bundle!.manifest.index.shards.every((shard) => assets.counts.get(shard.path) === 1)
      && assets.counts.get(bundle!.manifest.index.norms_path) === 1
      && assets.counts.get(bundle!.manifest.metadata.path) === 1
    const noFullFp32 = ![...assets.counts.keys()].some((path) => path.endsWith('.f32') && path !== bundle!.manifest.compatibility.path)
    const admission = handler!.admission.stats()
    const embeddingAdmission = embeddings.stats()
    const papers = bundle!.paperLoadStats()
    const largestPaperBytes = Math.max(...Object.entries(bundle!.manifest.files)
      .filter(([path]) => path.includes('/papers/')).map(([, value]) => value.bytes))
    const maxShard = Math.max(...bundle!.manifest.index.shards.map((shard) => shard.count * 768))
    const checks = {
      canonical_full_coverage: true,
      ...(options.dataLabel === 'geometry-fixture' ? {
        synthetic_provenance: bundle!.manifest.synthetic && !!bundle!.manifest.fixture_vectors && !bundle!.manifest.source_embeddings,
        production_rejects_fixture: productionRejectedFixture,
      } : {
        real_embedding_provenance: !bundle!.manifest.synthetic && !!bundle!.manifest.source_embeddings && !bundle!.manifest.fixture_vectors,
      }),
      observed_peak_below_local_threshold: summary.peaks.heap_plus_external < options.threshold,
      repeated_churn_retained_growth_bounded: retainedGrowth <= RETAINED_GROWTH_ALLOWANCE,
      singleton_initialization: serviceConstructions === 1 && binaryLoads,
      bounded_admission: admission.max_active <= limits.active && admission.active === 0
        && embeddingAdmission.max_active <= 2 && papers.peak_active <= papers.max_active,
      bounded_queue: admission.max_queued <= limits.queued && admission.queued === 0
        && embeddingAdmission.max_queued <= 2 && papers.pending === 0 && coldOverload >= 4 && sustainedOverload >= 32,
      structural_allocation_bound: binaryLoads && noFullFp32 && maxShard <= 4096 * 768
        && papers.max_active === 1 && papers.max_queued === 16,
      rest_wrapper: true, mcp_wrapper: true,
    }
    assert.deepEqual(sourceHashes(repo), sources, 'Implementation changed during the workload; rerun required')
    const passed = Object.values(checks).every(Boolean)
    Object.assign(report, {
      status: passed ? 'PASS' : 'FAIL', checks, local_checks: checks, summary,
      retained_growth: { bytes: retainedGrowth, allowance_bytes: RETAINED_GROWTH_ALLOWANCE, from: first.phase, to: second.phase },
      structural_allocation_account: {
        scope: 'Enforced structure/cardinality and binary byte bounds, not a complete V8 memory upper bound',
        resident_binary_bytes: bundle!.residentBinaryBytes, one_source_shard_bytes: maxShard,
        reference_sample_bytes: bundle!.manifest.files[bundle!.manifest.compatibility.path].bytes,
        largest_paper_json_bytes: largestPaperBytes,
        request_admission: admission, embedding_admission: embeddingAdmission, paper_admission: papers,
        request_body_limit_bytes: limits.request_bytes, response_body_limit_bytes: limits.response_bytes,
        body_buffering: 'At most 1024 chunks and 2x body byte limit while consolidating; response creation may copy again',
        paper_cache_entries: embed.limits.paper_cache_entries, paper_cache_text_utf8_bytes: embed.limits.paper_cache_bytes,
        search_cache_entries: embed.limits.search_cache_entries,
        unknowns: ['V8 object/string expansion', 'allocator/GC timing', 'crypto and stream native temporaries', 'Cloudflare accounting'],
      },
      resident_binary_bytes: bundle!.residentBinaryBytes, contract_requests: contractRequests,
      offline_embedding_calls: embeddedQueries, singleton_load_calls: loadCalls,
      asset_stats: assets.stats(), index_asset_read_counts: Object.fromEntries([...assets.counts].filter(([path]) => !path.includes('/papers/'))),
      inspector_after_workload: await inspectorUsage(),
      inspector_scope: 'Node V8 isolate only; not workerd or Cloudflare, not added to process memory totals',
    })
  } catch (error) {
    Object.assign(report, { status: 'FAIL', error: error instanceof Error ? error.message : String(error),
      failed_phase: phase, summary: summarizeSamples(samples), contract_requests: contractRequests,
      offline_embedding_calls: embeddedQueries, asset_stats: assets.stats() })
  } finally {
    if (timer) clearInterval(timer)
    Object.assign(report, { elapsed_ms: performance.now() - started, phases,
      sample_count_including_discarded_timer_samples: sampleCount,
      samples: samples.sort((a, b) => a.elapsed_ms - b.elapsed_ms) })
    await mkdir(dirname(options.out), { recursive: true })
    await writeFile(options.out, JSON.stringify(report, null, 2) + '\n')
  }
  return report
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const options = parseOptions(process.argv.slice(2))
  const report = await runMemoryHarness(options)
  process.stdout.write(JSON.stringify({ status: report.status, output: options.out,
    passages: report.passages, local_checks: report.local_checks }) + '\n')
  if (report.status !== 'PASS') process.exitCode = 1
}
