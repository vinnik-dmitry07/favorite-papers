import { handleRest, json } from './http'
import { handleMcp } from './mcp'
import { DomainError, errorBody } from './schemas'
import type { Service } from './service'

export const PROBE_REQUEST_LIMITS = Object.freeze({
  active: 4, queued: 8, queue_wait_ms: 2000,
  body_read_ms: 5000,
  request_bytes: 262144, response_bytes: 1048576, url_characters: 8192,
  header_characters: 16384, header_entries: 64,
})

interface Waiting {
  start(): void
  cleanup(): void
}

/** Admission is acquired before initialization, body buffering or embedding.
 * A timed-out/cancelled active task keeps its permit until the work settles.
 * This class cannot cancel underlying AI/provider work and never pretends to.
 */
export class BoundedAdmission {
  private active = 0
  private readonly waiting: Waiting[] = []
  private maxActive = 0
  private maxQueued = 0
  private rejected = 0
  private completed = 0

  constructor(readonly activeLimit: number, readonly queueLimit: number, readonly queueWaitMs = 2000) {
    if (!Number.isSafeInteger(activeLimit) || activeLimit < 1
      || !Number.isSafeInteger(queueLimit) || queueLimit < 0
      || !Number.isSafeInteger(queueWaitMs) || queueWaitMs < 1) throw new RangeError('Invalid admission bounds')
  }

  stats() {
    return { active: this.active, queued: this.waiting.length, max_active: this.maxActive,
      max_queued: this.maxQueued, rejected: this.rejected, completed: this.completed,
      active_limit: this.activeLimit, queue_limit: this.queueLimit, queue_wait_ms: this.queueWaitMs }
  }

  run<T>(work: () => Promise<T>, signal?: AbortSignal): Promise<T> {
    if (signal?.aborted) return Promise.reject(new DomainError('request_cancelled', 499, 'request cancelled'))
    if (this.active >= this.activeLimit && this.waiting.length >= this.queueLimit) {
      this.rejected++
      return Promise.reject(new DomainError('probe_overloaded', 503, 'probe admission queue is full'))
    }
    return new Promise<T>((resolve, reject) => {
      const start = () => {
        this.active++
        this.maxActive = Math.max(this.maxActive, this.active)
        void (async () => {
          let result: T | undefined
          let error: unknown
          let failed = false
          try { result = await work() } catch (caught) { error = caught; failed = true }
          finally {
            this.active--
            this.completed++
            const next = this.waiting.shift()
            if (next) { next.cleanup(); next.start() }
          }
          if (failed) reject(error)
          else resolve(result as T)
        })()
      }
      if (this.active < this.activeLimit) { start(); return }
      let timer: ReturnType<typeof setTimeout>
      const cancel = (error: DomainError) => {
        const index = this.waiting.indexOf(entry)
        if (index < 0) return
        this.waiting.splice(index, 1)
        entry.cleanup()
        this.rejected++
        reject(error)
      }
      const abort = () => cancel(new DomainError('request_cancelled', 499, 'queued request cancelled'))
      const entry: Waiting = { start, cleanup: () => {
        clearTimeout(timer)
        signal?.removeEventListener('abort', abort)
      } }
      timer = setTimeout(() => cancel(new DomainError('probe_overloaded', 503, 'probe admission wait expired')), this.queueWaitMs)
      signal?.addEventListener('abort', abort, { once: true })
      this.waiting.push(entry)
      this.maxQueued = Math.max(this.maxQueued, this.waiting.length)
    })
  }
}

async function boundedBody(body: ReadableStream<Uint8Array> | null, limit: number,
  signal?: AbortSignal, response = false): Promise<Uint8Array> {
  if (!body) return new Uint8Array()
  const reader = body.getReader()
  const parts: Uint8Array[] = []
  let size = 0
  let complete = false
  let abort!: () => void
  let timer!: ReturnType<typeof setTimeout>
  const interrupted = new Promise<never>((_resolve, reject) => {
    abort = () => reject(new DomainError('request_cancelled', 499, 'body read cancelled'))
    timer = setTimeout(() => reject(new DomainError(
      response ? 'response_timeout' : 'body_timeout', response ? 504 : 408,
      'probe body read deadline exceeded',
    )), PROBE_REQUEST_LIMITS.body_read_ms)
    signal?.addEventListener('abort', abort, { once: true })
    if (signal?.aborted) abort()
  })
  try {
    while (true) {
      const part = await Promise.race([reader.read(), interrupted])
      if (part.done) { complete = true; break }
      if (size + part.value.byteLength > limit || parts.length >= 1024) {
        throw new DomainError('body_too_large', 413, 'probe body exceeds its byte limit')
      }
      parts.push(part.value)
      size += part.value.byteLength
    }
    const output = new Uint8Array(size)
    let offset = 0
    for (const part of parts) { output.set(part, offset); offset += part.byteLength }
    return output
  } finally {
    clearTimeout(timer)
    signal?.removeEventListener('abort', abort)
    // Closing the reader stops our pending read. An underlying source's cancel
    // promise may never settle; it must not retain an admission permit.
    if (!complete) void reader.cancel().catch(() => {})
    reader.releaseLock()
  }
}

/** Isolated probe handler. This does not change the production Worker entrypoint.
 * Responses are fully serialized/byte bounded while holding admission, including
 * MCP's structuredContent plus text duplication. No arbitrary upstream fetches.
 */
export function createBoundedProbeHandler(loadService: () => Promise<Service>, admission = new BoundedAdmission(
  PROBE_REQUEST_LIMITS.active, PROBE_REQUEST_LIMITS.queued, PROBE_REQUEST_LIMITS.queue_wait_ms,
)) {
  return {
    admission,
    async fetch(request: Request): Promise<Response> {
      try {
        if (request.url.length > PROBE_REQUEST_LIMITS.url_characters) {
          throw new DomainError('invalid_argument', 414, 'probe URL exceeds its length limit')
        }
        let headerCharacters = 0, headerEntries = 0
        for (const [key, value] of request.headers) {
          headerCharacters += key.length + value.length
          headerEntries++
          if (headerCharacters > PROBE_REQUEST_LIMITS.header_characters || headerEntries > PROBE_REQUEST_LIMITS.header_entries) {
            throw new DomainError('invalid_argument', 431, 'probe headers exceed their limit')
          }
        }
        const declared = request.headers.get('content-length')
        if (declared !== null && (!/^\d+$/.test(declared)
          || Number(declared) > PROBE_REQUEST_LIMITS.request_bytes)) {
          throw new DomainError('body_too_large', 413, 'probe request exceeds its byte limit')
        }
        return await admission.run(async () => {
          let replay = request
          if (request.body) {
            const body = await boundedBody(request.body, PROBE_REQUEST_LIMITS.request_bytes, request.signal)
            replay = new Request(request.url, { method: request.method, headers: request.headers, body })
          }
          const service = await loadService()
          const response = new URL(request.url).pathname === '/mcp'
            ? await handleMcp(replay, service) : await handleRest(replay, service)
          const bytes = await boundedBody(response.body, PROBE_REQUEST_LIMITS.response_bytes, request.signal, true)
          return new Response(bytes, { status: response.status, headers: response.headers })
        }, request.signal)
      } catch (error) {
        if (request.body && !request.body.locked) void request.body.cancel().catch(() => {})
        const known = error instanceof DomainError ? error
          : new DomainError('corpus_unavailable', 503, 'probe request failed')
        const response = json(errorBody(known), known.status)
        if (known.code === 'probe_overloaded') response.headers.set('retry-after', '1')
        return response
      }
    },
  }
}
