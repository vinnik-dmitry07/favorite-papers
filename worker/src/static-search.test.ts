import { describe, expect, it } from 'vitest'

import { PqIndex, type PqConfig, type PqMatch } from './static-search'

function littleEndian(values: number[]): ArrayBuffer {
  const buffer = new ArrayBuffer(values.length * 4)
  const view = new DataView(buffer)
  values.forEach((value, index) => view.setFloat32(index * 4, value, true))
  return buffer
}

function fixture(overrides: Partial<PqConfig> = {}) {
  const config: PqConfig = {
    format: 'pq-ip-v1', dimensions: 4, subquantizers: 2, centroids: 3, count: 5,
    ...overrides,
  }
  const codes = Uint8Array.from([0, 0, 1, 2, 2, 1, 1, 0, 2, 2]).buffer
  const codebooks = littleEndian([1, 0, 0, 1, -1, 0.5, 0.5, -0.5, 0, 2, -1, -1])
  return { config, codes, codebooks }
}

// Independent oracle: reconstruct every quantized vector, calculate its full
// inner product, then sort all matches. Production never reconstructs vectors.
function reconstructedSearch(
  config: PqConfig, codes: ArrayBuffer, codebooks: ArrayBuffer, query: number[], topK: number,
): PqMatch[] {
  const rows = new Uint8Array(codes)
  const book = new DataView(codebooks)
  const subdimensions = config.dimensions / config.subquantizers
  const norm = Math.hypot(...query)
  const matches: PqMatch[] = []
  for (let index = 0; index < config.count; index++) {
    const reconstructed: number[] = []
    for (let sub = 0; sub < config.subquantizers; sub++) {
      const code = rows[index * config.subquantizers + sub]
      for (let dimension = 0; dimension < subdimensions; dimension++) {
        const offset = ((sub * config.centroids + code) * subdimensions + dimension) * 4
        reconstructed.push(book.getFloat32(offset, true))
      }
    }
    const score = reconstructed.reduce((sum, value, dimension) => sum + value * query[dimension] / norm, 0)
    matches.push({ index, score })
  }
  return matches.sort((left, right) => right.score - left.score || left.index - right.index).slice(0, topK)
}

function expectMatches(actual: PqMatch[], expected: PqMatch[]): void {
  expect(actual.map((match) => match.index)).toEqual(expected.map((match) => match.index))
  actual.forEach((match, index) => expect(match.score).toBeCloseTo(expected[index].score, 12))
}

describe('static PQ inner-product search', () => {
  it('matches independent full-vector reconstruction with a bounded top-k', () => {
    const { config, codes, codebooks } = fixture()
    const index = new PqIndex(config, codes, codebooks)
    for (const query of [[1, 2, -3, 4], [-2, 1, 3, -1], [1, 0, 0, 0]]) {
      for (const topK of [1, 2, 3, 5, 20]) {
        expectMatches(index.search(query, topK), reconstructedSearch(config, codes, codebooks, query, topK))
      }
    }
  })

  it('covers the 768-dimensional, 96-subquantizer, 256-centroid layout', () => {
    const config: PqConfig = {
      format: 'pq-ip-v1', dimensions: 768, subquantizers: 96, centroids: 256, count: 67,
    }
    const codes = Uint8Array.from(
      { length: config.count * config.subquantizers }, (_, index) => (index * 37 + (index >>> 3)) % 256,
    ).buffer
    const values = Array.from({ length: config.dimensions * config.centroids }, (_, index) => (
      ((index * 13 + (index >>> 7)) % 101 - 50) / 100
    ))
    const codebooks = littleEndian(values)
    const query = Array.from({ length: config.dimensions }, (_, index) => Math.sin(index + 0.25))
    const index = new PqIndex(config, codes, codebooks)
    expectMatches(index.search(query, 8), reconstructedSearch(config, codes, codebooks, query, 8))
  })

  it('handles divisible layouts including the remainder after unrolled scan groups', () => {
    for (const subquantizers of [1, 3, 4, 5, 7, 8]) {
      const config: PqConfig = {
        format: 'pq-ip-v1', dimensions: subquantizers * 2, subquantizers, centroids: 5, count: 23,
      }
      const codes = Uint8Array.from(
        { length: config.count * subquantizers }, (_, index) => (index * 3 + (index >>> 2)) % 5,
      ).buffer
      const codebooks = littleEndian(Array.from(
        { length: config.dimensions * config.centroids }, (_, index) => Math.cos(index) / 7,
      ))
      const query = Array.from({ length: config.dimensions }, (_, index) => index % 3 - 1)
      const index = new PqIndex(config, codes, codebooks)
      expectMatches(index.search(query, 9), reconstructedSearch(config, codes, codebooks, query, 9))
    }
  })

  it('normalizes queries without changing them or renormalizing PQ vectors', () => {
    const config: PqConfig = {
      format: 'pq-ip-v1', dimensions: 2, subquantizers: 1, centroids: 2, count: 2,
    }
    const index = new PqIndex(config, Uint8Array.from([0, 1]).buffer, littleEndian([3, 4, 0, 1]))
    const query = Float32Array.from([6, 8])
    expect(index.search(query, 2)).toEqual([{ index: 0, score: 5 }, { index: 1, score: 0.8 }])
    expect([...query]).toEqual([6, 8])
    expect(index.search([3, 4], 2)).toEqual(index.search(query, 2))
  })

  it('handles finite queries whose unscaled squared norm would overflow or underflow', () => {
    const { config, codes, codebooks } = fixture()
    const index = new PqIndex(config, codes, codebooks)
    const expected = index.search([1, -1, 1, -1], 3)
    expect(index.search([1e308, -1e308, 1e308, -1e308], 3)).toEqual(expected)
    expect(index.search([1e-320, -1e-320, 1e-320, -1e-320], 3)).toEqual(expected)
  })

  it('breaks ties by row index, including ties at the heap boundary', () => {
    const config: PqConfig = {
      format: 'pq-ip-v1', dimensions: 1, subquantizers: 1, centroids: 3, count: 8,
    }
    const codes = Uint8Array.from([0, 0, 1, 1, 1, 2, 2, 2]).buffer
    const index = new PqIndex(config, codes, littleEndian([0, 1, 2]))
    expect(index.search([1], 4)).toEqual([
      { index: 5, score: 2 }, { index: 6, score: 2 }, { index: 7, score: 2 }, { index: 2, score: 1 },
    ])
    expect(index.search([-1], 3)).toEqual([
      { index: 0, score: 0 }, { index: 1, score: 0 }, { index: 2, score: -1 },
    ])
  })

  it('decodes explicit little-endian float32 bytes', () => {
    const config: PqConfig = {
      format: 'pq-ip-v1', dimensions: 1, subquantizers: 1, centroids: 2, count: 2,
    }
    // 1.0 and -2.5 in IEEE 754 little-endian order, independent of host endian.
    const codebooks = Uint8Array.from([0, 0, 128, 63, 0, 0, 32, 192]).buffer
    const index = new PqIndex(config, Uint8Array.from([1, 0]).buffer, codebooks)
    expect(index.search([1], 2)).toEqual([{ index: 1, score: 1 }, { index: 0, score: -2.5 }])
  })

  it('keeps immutable copies of validated input buffers and configuration', () => {
    const { config, codes, codebooks } = fixture()
    const index = new PqIndex(config, codes, codebooks)
    const expected = index.search([1, 2, 3, 4], 3)
    new Uint8Array(codes).fill(255)
    new DataView(codebooks).setFloat32(0, NaN, true)
    config.count = 999
    expect(index.search([1, 2, 3, 4], 3)).toEqual(expected)
    expect(Object.isFrozen(index.config)).toBe(true)
  })

  it('allows an empty index and still validates the query and topK', () => {
    const { config, codebooks } = fixture({ count: 0 })
    const index = new PqIndex(config, new ArrayBuffer(0), codebooks)
    expect(index.search([1, 2, 3, 4], 1)).toEqual([])
    expect(() => index.search([0, 0, 0, 0], 1)).toThrow('nonzero norm')
    expect(() => index.search([1, 2, 3, 4], 0)).toThrow('topK')
  })

  it.each([0, -1, 0.5, 1001, NaN, Infinity])('rejects invalid topK %s', (topK) => {
    const { config, codes, codebooks } = fixture()
    expect(() => new PqIndex(config, codes, codebooks).search([1, 0, 0, 0], topK)).toThrow('topK')
  })

  it.each([
    [0, 0, 0, 0], [1, 0, 0], [NaN, 1, 0, 0], [Infinity, 0, 0, 0], [-Infinity, 0, 0, 0],
  ])('rejects invalid query %s', (...query) => {
    const { config, codes, codebooks } = fixture()
    expect(() => new PqIndex(config, codes, codebooks).search(query, 1)).toThrow()
  })

  it('rejects nonnumeric array values and sparse arrays', () => {
    const { config, codes, codebooks } = fixture()
    const index = new PqIndex(config, codes, codebooks)
    expect(() => index.search(['1', 0, 0, 0] as unknown as number[], 1)).toThrow('finite numbers')
    expect(() => index.search(new Array<number>(4), 1)).toThrow('finite numbers')
    expect(() => index.search(new Float64Array(4) as unknown as number[], 1)).toThrow('Float32Array')
  })

  it.each([
    { format: 'other' }, { dimensions: 0 }, { dimensions: 1537 }, { dimensions: 3 },
    { dimensions: 1.5 }, { subquantizers: 0 }, { subquantizers: 5 }, { centroids: 0 },
    { centroids: 257 }, { count: -1 }, { count: 1_000_001 }, { count: NaN }, { count: Infinity },
  ])('rejects malformed configuration %j', (overrides) => {
    const { config, codes, codebooks } = fixture(overrides as Partial<PqConfig>)
    expect(() => new PqIndex(config, codes, codebooks)).toThrow()
  })

  it('rejects oversized code payloads before allocating or reading data', () => {
    const { config } = fixture({ dimensions: 768, subquantizers: 96, count: 1_000_000 })
    expect(() => new PqIndex(config, new ArrayBuffer(0), new ArrayBuffer(0))).toThrow('byte limit')
  })

  it('rejects short and oversized code and codebook payloads', () => {
    const { config, codes, codebooks } = fixture()
    expect(() => new PqIndex(config, codes.slice(1), codebooks)).toThrow('codes must contain exactly')
    expect(() => new PqIndex(config, new ArrayBuffer(codes.byteLength + 1), codebooks)).toThrow('codes must contain exactly')
    expect(() => new PqIndex(config, codes, codebooks.slice(4))).toThrow('codebooks must contain exactly')
    expect(() => new PqIndex(config, codes, new ArrayBuffer(codebooks.byteLength + 4))).toThrow('codebooks must contain exactly')
  })

  it('rejects codes outside their subquantizer codebooks', () => {
    const { config, codes, codebooks } = fixture()
    new Uint8Array(codes)[3] = config.centroids
    expect(() => new PqIndex(config, codes, codebooks)).toThrow('nonexistent centroid')
  })

  it.each([NaN, Infinity, -Infinity])('rejects nonfinite codebook value %s', (value) => {
    const { config, codes, codebooks } = fixture()
    new DataView(codebooks).setFloat32(8, value, true)
    expect(() => new PqIndex(config, codes, codebooks)).toThrow('finite float32')
  })

  it('keeps valid large float32 codebooks finite through lookup accumulation', () => {
    const config: PqConfig = {
      format: 'pq-ip-v1', dimensions: 4, subquantizers: 1, centroids: 1, count: 1,
    }
    const index = new PqIndex(config, new ArrayBuffer(1), littleEndian([3e38, 3e38, 3e38, 3e38]))
    const [match] = index.search([1, 1, 1, 1], 1)
    expect(Number.isFinite(match.score)).toBe(true)
    expect(match.score).toBeGreaterThan(3.5e38)
  })
})
