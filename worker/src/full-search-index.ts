import { selectTop } from './static-search-int8'

export interface FullIndexManifest {
  passage_count: number
  dimensions: number
  index: {
    kind: 'exact-int8'
    quantization: 'per-row-maxabs-rint-127'
    norms_path: string
    shards: { path: string, start: number, count: number }[]
  }
}

export interface IndexMemorySample {
  phase: string
  resident_index_bytes: number
  current_asset_bytes: number
}

/** Exact cosine over quantized rows. No sign-bit or approximate shortlist stage.
 * Rows are packed in vector-ID order, so ties by row index are ties by ID.
 * The loader must authenticate each asset and must not retain downloaded buffers.
 */
export class FullSearchIndex {
  private readonly buffer: ArrayBuffer
  private readonly normsOffset: number
  private readonly queryOffset: number
  private readonly outputOffset: number
  private readonly kernel?: (...args: number[]) => void
  readonly residentBytes: number

  private constructor(readonly count: number, readonly dimensions: number, module?: WebAssembly.Module) {
    if (!Number.isSafeInteger(count) || count < 1 || count > 60000 || dimensions !== 768) {
      throw new RangeError('Invalid full-index geometry')
    }
    this.normsOffset = Math.ceil(count * dimensions / 8) * 8
    this.queryOffset = this.normsOffset + count * 8
    this.outputOffset = this.queryOffset + dimensions * 8
    const needed = this.outputOffset + count * 8
    if (module) {
      const exports = new WebAssembly.Instance(module).exports as {
        memory: WebAssembly.Memory, int8: (...args: number[]) => void,
      }
      if (!(exports.memory instanceof WebAssembly.Memory) || typeof exports.int8 !== 'function') {
        throw new RangeError('Missing exact int8 WASM kernel')
      }
      const pages = Math.ceil(needed / 65536)
      const current = exports.memory.buffer.byteLength / 65536
      if (pages > current) exports.memory.grow(pages - current)
      this.buffer = exports.memory.buffer
      this.kernel = exports.int8
    } else {
      this.buffer = new ArrayBuffer(needed)
    }
    this.residentBytes = this.buffer.byteLength
  }

  static async load(
    manifest: FullIndexManifest,
    loadAsset: (path: string) => Promise<ArrayBuffer>,
    module?: WebAssembly.Module,
    memorySample?: (sample: IndexMemorySample) => void,
  ): Promise<FullSearchIndex> {
    if (manifest.index.kind !== 'exact-int8'
      || manifest.index.quantization !== 'per-row-maxabs-rint-127') {
      throw new RangeError('Unsupported full-index quantization')
    }
    const result = new FullSearchIndex(manifest.passage_count, manifest.dimensions, module)
    const sample = (phase: string, bytes = 0) => memorySample?.({
      phase, resident_index_bytes: result.residentBytes, current_asset_bytes: bytes,
    })
    sample('allocated')
    // A function scope releases each source buffer before the next fetch. No
    // Promise.all and no buffer cache: initialization retains only one shard.
    const copyShard = async (path: string, offset: number, expected: number) => {
      const bytes = await loadAsset(path)
      if (bytes.byteLength !== expected) throw new RangeError('Wrong int8 asset length')
      sample('asset-loaded:' + path, bytes.byteLength)
      new Uint8Array(result.buffer, offset, expected).set(new Uint8Array(bytes))
      sample('asset-copied:' + path, bytes.byteLength)
    }
    let next = 0
    for (const shard of manifest.index.shards) {
      if (shard.start !== next || !Number.isSafeInteger(shard.count)
        || shard.count < 1 || shard.count > 4096
        || next + shard.count > result.count) throw new RangeError('Noncontiguous vector shards')
      await copyShard(shard.path, next * result.dimensions, shard.count * result.dimensions)
      next += shard.count
    }
    if (next !== result.count) throw new RangeError('Incomplete vector index')
    await copyShard(manifest.index.norms_path, result.normsOffset, result.count * 8)
    // Norms are always little-endian, including on a hypothetical BE host.
    const view = new DataView(result.buffer)
    const norms = new Float64Array(result.buffer, result.normsOffset, result.count)
    const integers = new Int8Array(result.buffer, 0, result.count * result.dimensions)
    for (let row = 0; row < result.count; row++) {
      const inverse = view.getFloat64(result.normsOffset + row * 8, true)
      let squared = 0
      for (let dim = 0; dim < result.dimensions; dim++) {
        const value = integers[row * result.dimensions + dim]
        if (value === -128) throw new RangeError('Invalid symmetric int8 value')
        squared += value * value
      }
      if (!Number.isFinite(inverse) || inverse <= 0 || !squared
        || Math.abs(inverse * Math.sqrt(squared) - 1) > 1e-10) {
        throw new RangeError('Int8 normalization mismatch')
      }
      // WASM memory is LE; JS typed arrays use native endianness. All supported
      // Workers targets are LE, checked explicitly to avoid silent corruption.
      norms[row] = inverse
    }
    if (new Uint8Array(new Uint16Array([1]).buffer)[0] !== 1) {
      throw new RangeError('Full int8 index requires a little-endian runtime')
    }
    sample('ready')
    return result
  }

  search(query: ArrayLike<number>, k: number): { index: number, score: number }[] {
    if (query.length !== this.dimensions || !Number.isSafeInteger(k) || k < 1 || k > 1000) {
      throw new RangeError('Invalid full-index query')
    }
    let squared = 0
    for (let dim = 0; dim < this.dimensions; dim++) {
      const value = query[dim]
      if (typeof value !== 'number' || !Number.isFinite(value)) throw new RangeError('Non-finite query')
      squared += value * value
    }
    const norm = Math.sqrt(squared)
    if (!Number.isFinite(norm) || !norm) throw new RangeError('Invalid query norm')
    const normalized = new Float64Array(this.buffer, this.queryOffset, this.dimensions)
    for (let dim = 0; dim < this.dimensions; dim++) normalized[dim] = query[dim] / norm
    const scores = new Float64Array(this.buffer, this.outputOffset, this.count)
    if (this.kernel) {
      this.kernel(0, this.queryOffset, this.normsOffset, this.outputOffset, 0, this.count, this.dimensions)
    } else {
      const vectors = new Int8Array(this.buffer, 0, this.count * this.dimensions)
      const norms = new Float64Array(this.buffer, this.normsOffset, this.count)
      for (let row = 0; row < this.count; row++) {
        let dot = 0
        for (let dim = 0; dim < this.dimensions; dim++) dot += vectors[row * this.dimensions + dim] * normalized[dim]
        scores[row] = dot * norms[row]
      }
    }
    return selectTop(scores, Math.min(k, this.count))
  }
}
