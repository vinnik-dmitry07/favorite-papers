/** Product-quantized inner-product search over an immutable, static index. */
export interface PqConfig {
  format: 'pq-ip-v1'
  dimensions: number
  subquantizers: number
  centroids: number
  count: number
}

export interface PqMatch {
  index: number
  score: number
}

const MAX_DIMENSIONS = 1536
const MAX_COUNT = 1_000_000
const MAX_CODE_BYTES = 64 * 1024 * 1024
const MAX_TOP_K = 1000
const LITTLE_ENDIAN_HOST = new Uint8Array(new Uint16Array([1]).buffer)[0] === 1

function integerInRange(value: number, min: number, max: number, name: string): void {
  if (!Number.isSafeInteger(value) || value < min || value > max) {
    throw new RangeError(`${name} must be an integer between ${min} and ${max}`)
  }
}

// The heap root is the worst retained match: lowest score, then highest index.
function worse(score: number, index: number, otherScore: number, otherIndex: number): boolean {
  return score < otherScore || (score === otherScore && index > otherIndex)
}

/**
 * Codes are uint8, row-major [count, subquantizers]. Codebooks are explicitly
 * little-endian float32, ordered [subquantizers, centroids, dimensions / M].
 * The constructor takes private copies so later buffer mutation cannot invalidate
 * validation. Asset loading and query embedding are the caller's responsibility.
 *
 * Scores approximate inner products with the original normalized embeddings.
 * They are NOT exact cosine similarities: reconstructed PQ vectors are not
 * renormalized. Training must use the same embedding normalization and format.
 */
export class PqIndex {
  readonly config: Readonly<PqConfig>
  private readonly codes: Uint8Array
  private readonly codebooks: Float32Array
  private readonly subdimensions: number

  constructor(config: PqConfig, codes: ArrayBuffer, codebooks: ArrayBuffer) {
    if (!config || config.format !== 'pq-ip-v1') {
      throw new TypeError('Unsupported PQ format; expected pq-ip-v1')
    }
    integerInRange(config.dimensions, 1, MAX_DIMENSIONS, 'dimensions')
    integerInRange(config.subquantizers, 1, config.dimensions, 'subquantizers')
    integerInRange(config.centroids, 1, 256, 'centroids')
    integerInRange(config.count, 0, MAX_COUNT, 'count')
    if (config.dimensions % config.subquantizers !== 0) {
      throw new RangeError('dimensions must be divisible by subquantizers')
    }
    const codeBytes = config.count * config.subquantizers
    if (codeBytes > MAX_CODE_BYTES) {
      throw new RangeError(`PQ codes exceed the ${MAX_CODE_BYTES}-byte limit`)
    }
    if (!(codes instanceof ArrayBuffer) || codes.byteLength !== codeBytes) {
      throw new RangeError(`PQ codes must contain exactly ${codeBytes} bytes`)
    }
    const codebookBytes = config.dimensions * config.centroids * Float32Array.BYTES_PER_ELEMENT
    if (!(codebooks instanceof ArrayBuffer) || codebooks.byteLength !== codebookBytes) {
      throw new RangeError(`PQ codebooks must contain exactly ${codebookBytes} bytes`)
    }

    this.config = Object.freeze({
      format: config.format,
      dimensions: config.dimensions,
      subquantizers: config.subquantizers,
      centroids: config.centroids,
      count: config.count,
    })
    this.subdimensions = config.dimensions / config.subquantizers
    this.codes = new Uint8Array(codes.slice(0))
    if (config.centroids < 256) {
      for (const code of this.codes) {
        if (code >= config.centroids) {
          throw new RangeError('PQ code references a nonexistent centroid')
        }
      }
    }

    this.codebooks = new Float32Array(codebooks.slice(0))
    if (!LITTLE_ENDIAN_HOST) {
      const view = new DataView(codebooks)
      for (let index = 0; index < this.codebooks.length; index++) {
        this.codebooks[index] = view.getFloat32(index * Float32Array.BYTES_PER_ELEMENT, true)
      }
    }
    for (let index = 0; index < this.codebooks.length; index++) {
      if (!Number.isFinite(this.codebooks[index])) {
        throw new RangeError('PQ codebooks must contain only finite float32 values')
      }
    }
  }

  search(query: Float32Array | number[], topK: number): PqMatch[] {
    integerInRange(topK, 1, MAX_TOP_K, 'topK')
    if (!(query instanceof Float32Array) && !Array.isArray(query)) {
      throw new TypeError('query must be a Float32Array or number array')
    }
    if (query.length !== this.config.dimensions) {
      throw new RangeError(`query must have ${this.config.dimensions} dimensions`)
    }

    // Scale first so finite inputs near the limits of float64 neither overflow
    // the norm nor underflow to zero. Do not mutate the caller's query.
    let scale = 0
    for (let dimension = 0; dimension < query.length; dimension++) {
      const value = query[dimension]
      if (!Number.isFinite(value)) {
        throw new RangeError('query must contain only finite numbers')
      }
      scale = Math.max(scale, Math.abs(value))
    }
    if (scale === 0) throw new RangeError('query must have a nonzero norm')
    let squaredNorm = 0
    const normalized = new Float64Array(query.length)
    for (let dimension = 0; dimension < query.length; dimension++) {
      const value = query[dimension] / scale
      normalized[dimension] = value
      squaredNorm += value * value
    }
    const norm = Math.sqrt(squaredNorm)
    for (let dimension = 0; dimension < normalized.length; dimension++) {
      normalized[dimension] /= norm
    }

    const { count, subquantizers, centroids } = this.config
    const limit = Math.min(topK, count)
    if (limit === 0) return []

    // Float64 accumulation avoids float32 overflow and unnecessary rounding
    // for otherwise valid finite codebooks. Only M * K values are calculated.
    const lookup = new Float64Array(subquantizers * centroids)
    let bookOffset = 0
    let lookupOffset = 0
    for (let sub = 0; sub < subquantizers; sub++) {
      const queryOffset = sub * this.subdimensions
      for (let centroid = 0; centroid < centroids; centroid++) {
        let score = 0
        for (let dimension = 0; dimension < this.subdimensions; dimension++) {
          score += normalized[queryOffset + dimension] * this.codebooks[bookOffset++]
        }
        lookup[lookupOffset++] = score
      }
    }

    const heapScores = new Float64Array(limit)
    const heapIndices = new Uint32Array(limit)
    const codes = this.codes
    const twiceCentroids = centroids * 2
    const tripleCentroids = centroids * 3
    const fourCentroids = centroids * 4
    const unrolledSubquantizers = subquantizers - subquantizers % 4
    let heapSize = 0
    let codeOffset = 0
    for (let index = 0; index < count; index++) {
      let score = 0
      let sub = 0
      let tableOffset = 0
      // Four consecutive additions preserve the accumulation order while
      // reducing loop overhead for the default 96-subquantizer layout.
      for (; sub < unrolledSubquantizers; sub += 4, tableOffset += fourCentroids) {
        score += lookup[tableOffset + codes[codeOffset++]]
        score += lookup[tableOffset + centroids + codes[codeOffset++]]
        score += lookup[tableOffset + twiceCentroids + codes[codeOffset++]]
        score += lookup[tableOffset + tripleCentroids + codes[codeOffset++]]
      }
      for (; sub < subquantizers; sub++, tableOffset += centroids) {
        score += lookup[tableOffset + codes[codeOffset++]]
      }

      if (heapSize < limit) {
        let position = heapSize++
        while (position > 0) {
          const parent = (position - 1) >>> 1
          if (!worse(score, index, heapScores[parent], heapIndices[parent])) break
          heapScores[position] = heapScores[parent]
          heapIndices[position] = heapIndices[parent]
          position = parent
        }
        heapScores[position] = score
        heapIndices[position] = index
        continue
      }

      // Rows arrive in ascending index order, so an equal score cannot beat
      // an existing match. No allocation occurs for rejected candidates.
      if (score <= heapScores[0]) continue
      let position = 0
      while (true) {
        let child = position * 2 + 1
        if (child >= limit) break
        const right = child + 1
        if (right < limit && worse(
          heapScores[right], heapIndices[right], heapScores[child], heapIndices[child],
        )) child = right
        if (!worse(heapScores[child], heapIndices[child], score, index)) break
        heapScores[position] = heapScores[child]
        heapIndices[position] = heapIndices[child]
        position = child
      }
      heapScores[position] = score
      heapIndices[position] = index
    }

    const matches: PqMatch[] = []
    for (let position = 0; position < heapSize; position++) {
      matches.push({ index: heapIndices[position], score: heapScores[position] })
    }
    return matches.sort((left, right) => right.score - left.score || left.index - right.index)
  }
}
