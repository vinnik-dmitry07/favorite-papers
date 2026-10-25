import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import { fullCorpusFixture } from '../test-fixtures/full-corpus'
import { createFullCorpusStore, createGeometryFixtureStore, createGeometryFixtureStoreLoader } from './full-corpus-store'

const module = new WebAssembly.Module(readFileSync(new URL('../probe-kernel/scan.wasm', import.meta.url)))
const options = { module }

describe('full corpus packed admission and mapping', () => {
  it('rejects honest synthetic data in the real loader and fake BGE identity in fixture loader', async () => {
    const data = await fullCorpusFixture()
    await expect(createFullCorpusStore(data.assets, data.manifestSha, async () => data.query, undefined, options))
      .rejects.toThrow('unsupported manifest')
    data.manifest.source_embeddings = { model_id: 'BAAI/bge-base-en-v1.5', model_revision: 'fake',
      pooling: 'cls', normalization: 'l2', dtype: 'float32', byte_order: 'little',
      count: data.rows.length, dimensions: 768, sha256: '0'.repeat(64) }
    await expect(createGeometryFixtureStore(data.assets, await data.syncManifest(), async () => data.query, undefined, options))
      .rejects.toThrow('synthetic geometry provenance')
  })

  it('preserves source mapping, Unicode code-point offsets and deterministic ties across top25/top40', async () => {
    const data = await fullCorpusFixture()
    const bundle = await createGeometryFixtureStore(data.assets, data.manifestSha, async () => data.query, undefined, options)
    for (const [index, expected] of data.packedRows.entries()) {
      expect(bundle.readRow(index)).toEqual(expected)
      expect(data.rows[expected.sourceIndex]).toEqual(expected)
    }
    for (const k of [25, 40, 50, 60]) {
      const hits = await bundle.store.query('full-probe', data.query, k)
      expect(hits.map((hit) => hit.id)).toEqual(data.packedRows.slice(0, k).map((row) => row.id))
      expect(hits.every((hit) => Math.abs(hit.score - 1) < 1e-12)).toBe(true)
    }
    const source = data.packedRows.findIndex((row) => row.chunk_index === 2)
    const ref = await bundle.referencePassage(source)
    const doc = data.papers.get(ref.row.paper_id)!
    expect(ref.vector).toEqual(data.query)
    expect(ref.input).toEqual([...doc.text].slice(ref.row.start, ref.row.end).join(''))
    expect(ref.input).toContain('😀')
    expect(bundle.manifest.synthetic).toBe(true)
    expect(new Set(data.packedRows.slice(0, 25).map((row) => row.paper_id)).size).toBeGreaterThanOrEqual(9)
  })

  it('shares one initialization promise and one index across simultaneous cold callers', async () => {
    const data = await fullCorpusFixture()
    const get = createGeometryFixtureStoreLoader(data.assets, data.manifestSha, async () => data.query, undefined, options)
    const promises = Array.from({ length: 20 }, () => get())
    expect(promises.every((promise) => promise === promises[0])).toBe(true)
    const bundles = await Promise.all(promises)
    expect(bundles.every((bundle) => bundle === bundles[0])).toBe(true)
    for (const path of ['probe.json', 'metadata.bin', 'norms.f64', 'vectors-0000.i8']) expect(data.reads.get(path)).toBe(1)
  })

  it('retains initialization failure to prevent retry allocation storms', async () => {
    const data = await fullCorpusFixture()
    data.files.delete('vectors-0000.i8')
    const get = createGeometryFixtureStoreLoader(data.assets, data.manifestSha, async () => data.query, undefined, options)
    await expect(get()).rejects.toThrow('missing asset')
    await expect(get()).rejects.toThrow('missing asset')
    expect(data.reads.get('probe.json')).toBe(1)
    expect(data.reads.get('vectors-0000.i8')).toBe(1)
  })

  it.each(['checksum', 'offset', 'source', 'source-permutation', 'norm', 'short-shard'])('rejects authenticated or raw corruption: %s', async (change) => {
    const data = await fullCorpusFixture()
    let sha = data.manifestSha
    if (change === 'checksum') data.files.get('metadata.bin')![0] ^= 1
    else {
      const path = change === 'norm' ? 'norms.f64' : change === 'short-shard' ? 'vectors-0000.i8' : 'metadata.bin'
      let bytes = data.files.get(path)!.slice()
      const view = new DataView(bytes.buffer)
      if (change === 'offset') view.setUint32(44, 0xffffffff, true)
      if (change === 'source') view.setUint32(52, view.getUint32(128 + 52, true), true)
      if (change === 'source-permutation') {
        const old = view.getUint32(52, true)
        view.setUint32(52, view.getUint32(128 + 52, true), true)
        view.setUint32(128 + 52, old, true)
      }
      if (change === 'norm') view.setFloat64(0, 1, true)
      if (change === 'short-shard') bytes = bytes.slice(1)
      await data.put(path, bytes); sha = await data.syncManifest()
    }
    await expect(createGeometryFixtureStore(data.assets, sha, async () => data.query, undefined, options)).rejects.toThrow()
  })

  it('bounds distinct paper validations and deduplicates same-paper waiters before any load', async () => {
    const data = await fullCorpusFixture(20)
    let release!: () => void
    const barrier = new Promise<void>((resolve) => { release = resolve })
    let streams = 0, peakStreams = 0
    const assets = { async fetch(request: Request) {
      if (new URL(request.url).pathname.includes('/papers/')) {
        streams++; peakStreams = Math.max(peakStreams, streams)
        await barrier
        try { return await data.assets.fetch(request) } finally { streams-- }
      }
      return data.assets.fetch(request)
    } }
    const bundle = await createGeometryFixtureStore(assets, data.manifestSha, async () => data.query, undefined, options)
    const paths = [...data.paperPaths.values()]
    const pending = paths.map((path) => bundle.store.getJson(path))
    const repeated = bundle.store.getJson(paths[0])
    const outcomes = Promise.allSettled(pending)
    await new Promise((resolve) => setTimeout(resolve, 0))
    expect(bundle.paperLoadStats()).toMatchObject({ active: 1, queued: 16, pending: 17, rejected: 3 })
    expect(peakStreams).toBe(1)
    release()
    const results = await outcomes
    expect(results.filter((result) => result.status === 'fulfilled')).toHaveLength(17)
    expect(results.filter((result) => result.status === 'rejected')).toHaveLength(3)
    for (const result of results) if (result.status === 'rejected') expect(result.reason).toMatchObject({ code: 'overloaded', status: 503 })
    await repeated
    expect(data.reads.get(paths[0])).toBe(1)
    expect(bundle.paperLoadStats()).toMatchObject({ active: 0, queued: 0, pending: 0, peak_active: 1 })
  })
})
