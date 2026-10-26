import { describe, expect, it } from 'vitest'

import { validProbeToken } from './probe-auth'

const TOKEN = 'test-token-with-at-least-32-characters'

describe('probe token comparison', () => {
  it('accepts identical tokens and rejects same-length changes at either end', () => {
    expect(validProbeToken(TOKEN, TOKEN)).toBe(true)
    expect(validProbeToken(TOKEN, 'x' + TOKEN.slice(1))).toBe(false)
    expect(validProbeToken(TOKEN, TOKEN.slice(0, -1) + 'x')).toBe(false)
  })

  it('rejects missing, short, overlong and differently encoded values without throwing', () => {
    for (const expected of [undefined, null, '', 'short', 'x'.repeat(257)]) {
      expect(validProbeToken(expected, TOKEN)).toBe(false)
    }
    for (const supplied of [null, '', 'short', 'x'.repeat(257), 'é'.repeat(TOKEN.length)]) {
      expect(validProbeToken(TOKEN, supplied)).toBe(false)
    }
  })
})
