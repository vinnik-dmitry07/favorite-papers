import type { PqConfig, PqScorer } from './static-search'

/** A per-index instance. Code bytes are copied only once; queries copy the LUT. */
export class WasmPqScorer implements PqScorer {
  private readonly exports: { memory: WebAssembly.Memory, pq: (...args: number[]) => void }
  private codes: Uint8Array | undefined
  private lutOffset = 0
  private outOffset = 0

  constructor(module: WebAssembly.Module) {
    this.exports = new WebAssembly.Instance(module).exports as typeof this.exports
  }

  score(codes: Uint8Array, lookup: Float64Array, config: Readonly<PqConfig>): Float64Array {
    const { memory, pq } = this.exports
    if (this.codes !== codes) {
      this.lutOffset = Math.ceil(codes.length / 8) * 8
      this.outOffset = this.lutOffset + lookup.byteLength
      const needed = this.outOffset + config.count * 8
      if (needed > 64 * 1024 * 1024) throw new RangeError('WASM probe memory exceeds 64 MiB')
      if (memory.buffer.byteLength < needed) memory.grow(Math.ceil((needed - memory.buffer.byteLength) / 65536))
      new Uint8Array(memory.buffer, 0, codes.length).set(codes)
      this.codes = codes
    }
    new Float64Array(memory.buffer, this.lutOffset, lookup.length).set(lookup)
    pq(0, this.lutOffset, this.outOffset, config.count, config.subquantizers, config.centroids)
    return new Float64Array(memory.buffer, this.outOffset, config.count)
  }
}
