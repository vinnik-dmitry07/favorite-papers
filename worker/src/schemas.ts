import { embed } from './tokenize'

export class DomainError extends Error {
  constructor(
    readonly code: string,
    readonly status: number,
    message: string,
    readonly details: Record<string, unknown> = {},
  ) {
    super(message)
    this.name = 'DomainError'
  }
}

export function fail(
  code: string,
  status: number,
  message: string,
  details: Record<string, unknown> = {},
): never {
  throw new DomainError(code, status, message, details)
}

export function errorBody(error: DomainError): {
  error: { code: string, message: string, details: Record<string, unknown> }
} {
  return {
    error: {
      code: error.code,
      message: error.message,
      details: error.details,
    },
  }
}

export function parseId(value: unknown): string {
  if (typeof value !== 'string' || value.length === 0) {
    fail('invalid_argument', 400, 'id is required', { field: 'id' })
  }
  const bytes = new TextEncoder().encode(value).length
  if (bytes > embed.limits.id_bytes_max) {
    fail('invalid_argument', 400, `id exceeds ${embed.limits.id_bytes_max} bytes`, { field: 'id' })
  }
  return value
}

export function parseBoundedInt(
  value: unknown,
  fallback: number,
  min: number,
  max: number,
  field: string,
): number {
  if (value === undefined || value === null || value === '') {
    return fallback
  }
  let parsed: number
  if (typeof value === 'number') {
    if (!Number.isFinite(value) || !Number.isInteger(value)) {
      fail('invalid_argument', 400, `${field} must be an integer`, { field })
    }
    parsed = value
  } else if (typeof value === 'string') {
    if (!/^-?\d+$/.test(value)) {
      fail('invalid_argument', 400, `${field} must be an integer`, { field })
    }
    parsed = Number(value)
    if (!Number.isSafeInteger(parsed)) {
      fail('invalid_argument', 400, `${field} must be an integer`, { field })
    }
  } else {
    fail('invalid_argument', 400, `${field} must be an integer`, { field })
  }
  if (parsed < min || parsed > max) {
    fail('invalid_argument', 400, `${field} is outside ${min}..${max}`, { field })
  }
  return parsed
}

export function parseDirection(value: unknown): 'out' | 'in' | 'both' {
  const raw = value === undefined || value === null || value === '' ? 'out' : value
  if (raw !== 'out' && raw !== 'in' && raw !== 'both') {
    fail('invalid_argument', 400, 'dir must be out, in, or both', { field: 'dir' })
  }
  return raw
}

export function parseOffset(value: unknown): number {
  if (value === undefined || value === null || value === '') {
    return 0
  }
  if (typeof value === 'number') {
    if (!Number.isFinite(value) || !Number.isInteger(value)) {
      fail('invalid_offset', 400, 'offset must be an integer', { field: 'offset' })
    }
    if (value < 0) {
      fail('invalid_offset', 400, 'offset must be >= 0', { field: 'offset' })
    }
    return value
  }
  if (typeof value !== 'string' || !/^\d+$/.test(value)) {
    fail('invalid_offset', 400, 'offset must be an integer', { field: 'offset' })
  }
  const parsed = Number(value)
  if (!Number.isSafeInteger(parsed)) {
    fail('invalid_offset', 400, 'offset must be an integer', { field: 'offset' })
  }
  return parsed
}
