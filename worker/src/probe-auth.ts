import { timingSafeEqual } from 'node:crypto'

const encoder = new TextEncoder()

/** Tokens have public, bounded lengths; compare their contents in native code. */
export function validProbeToken(expected: unknown, supplied: string | null): boolean {
  if (typeof expected !== 'string' || expected.length < 32 || expected.length > 256
      || supplied === null || supplied.length > 256) return false
  const expectedBytes = encoder.encode(expected)
  const suppliedBytes = encoder.encode(supplied)
  return expectedBytes.byteLength === suppliedBytes.byteLength
    && timingSafeEqual(expectedBytes, suppliedBytes)
}
