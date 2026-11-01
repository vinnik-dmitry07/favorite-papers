import type { PqMatch } from './static-search'

/** Bounded heap selection; score order and tie rule match the PQ kernel. */
export function selectTop(scores: Float64Array, k: number, ids?: number[]): PqMatch[] {
  const heap: PqMatch[] = []
  const worse = (a: PqMatch, b: PqMatch) => a.score < b.score || (a.score === b.score && a.index > b.index)
  for (let i = 0; i < scores.length; i++) {
    const index = ids?.[i] ?? i
    const score = scores[i]
    if (heap.length === k && (score < heap[0].score || (score === heap[0].score && index >= heap[0].index))) continue
    const item = { index, score }
    if (heap.length < k) {
      let at = heap.length
      heap.push(item)
      while (at > 0) {
        const parent = (at - 1) >>> 1
        if (!worse(item, heap[parent])) break
        heap[at] = heap[parent]; at = parent
      }
      heap[at] = item
    } else {
      let at = 0
      while (at * 2 + 1 < k) {
        let child = at * 2 + 1
        if (child + 1 < k && worse(heap[child + 1], heap[child])) child++
        if (!worse(heap[child], item)) break
        heap[at] = heap[child]; at = child
      }
      heap[at] = item
    }
  }
  return heap.sort((a, b) => b.score - a.score || a.index - b.index)
}

/** Scalar WASM int8 baseline and sign-bit candidate selection. No FP32 claim. */
export class Int8Index {
  private readonly exports: { memory: WebAssembly.Memory, int8: (...args: number[]) => void, binary: (...args: number[]) => void }
  private readonly normsOffset: number
  private readonly bitsOffset: number
  private readonly queryOffset: number
  private readonly idsOffset: number
  private readonly outputOffset: number

  constructor(module: WebAssembly.Module, private readonly count: number, private readonly dimensions: number,
    vectors: ArrayBuffer[], norms: ArrayBuffer, bits: ArrayBuffer) {
    if (!Number.isSafeInteger(count) || count < 1 || count > 1000000
      || !Number.isSafeInteger(dimensions) || dimensions < 32 || dimensions > 1536 || dimensions % 32
      || vectors.reduce((n, data) => n + data.byteLength, 0) !== count * dimensions
      || norms.byteLength !== count * 8 || bits.byteLength !== count * dimensions / 8) {
      throw new RangeError('Invalid int8 probe geometry')
    }
    const normView = new DataView(norms)
    for (let i = 0; i < count; i++) {
      const value = normView.getFloat64(i * 8, true)
      if (!Number.isFinite(value) || value <= 0) throw new RangeError('Invalid int8 norm')
    }
    this.normsOffset = Math.ceil(count * dimensions / 8) * 8
    this.bitsOffset = this.normsOffset + norms.byteLength
    this.queryOffset = Math.ceil((this.bitsOffset + bits.byteLength) / 8) * 8
    this.idsOffset = this.queryOffset + dimensions * 8
    this.outputOffset = Math.ceil((this.idsOffset + count * 4) / 8) * 8
    const needed = this.outputOffset + count * 8
    if (needed > 64 * 1024 * 1024) throw new RangeError('int8 memory exceeds 64 MiB')
    this.exports = new WebAssembly.Instance(module).exports as typeof this.exports
    this.exports.memory.grow(Math.ceil(needed / 65536) - 1)
    const data = new Uint8Array(this.exports.memory.buffer)
    let offset = 0
    for (const vector of vectors) { data.set(new Uint8Array(vector), offset); offset += vector.byteLength }
    data.set(new Uint8Array(norms), this.normsOffset)
    data.set(new Uint8Array(bits), this.bitsOffset)
  }

  search(query: Float32Array, k: number, candidates?: number[], binaryCandidates = false): PqMatch[] {
    if (query.length !== this.dimensions || query.some((value) => !Number.isFinite(value))) throw new RangeError('Invalid query')
    if (!Number.isSafeInteger(k) || k < 1 || k > 1000) throw new RangeError('Invalid topK')
    if (candidates?.some((i) => !Number.isInteger(i) || i < 0 || i >= this.count)
      || (candidates && candidates.length > this.count)) throw new RangeError('Invalid candidates')
    const norm = Math.hypot(...query)
    if (!norm) throw new RangeError('Zero query')
    const memory = this.exports.memory.buffer
    if (binaryCandidates) {
      const bits = new Uint8Array(memory, this.queryOffset, this.dimensions / 8)
      bits.fill(0)
      for (let i = 0; i < query.length; i++) if (query[i] >= 0) bits[i >>> 3] |= 1 << (i % 8)
      this.exports.binary(this.bitsOffset, this.queryOffset, this.outputOffset, this.count, this.dimensions / 32)
      candidates = selectTop(new Float64Array(memory, this.outputOffset, this.count), Math.min(200, this.count)).map((hit) => hit.index)
    }
    new Float64Array(memory, this.queryOffset, this.dimensions).set(Array.from(query, (value) => value / norm))
    if (candidates) new Uint32Array(memory, this.idsOffset, candidates.length).set(candidates)
    const count = candidates?.length ?? this.count
    this.exports.int8(0, this.queryOffset, this.normsOffset, this.outputOffset, candidates ? this.idsOffset : 0, count, this.dimensions)
    return selectTop(new Float64Array(memory, this.outputOffset, count), k, candidates)
  }
}
