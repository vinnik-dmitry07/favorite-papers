import { afterEach, describe, expect, it, vi } from 'vitest'
import { BoundedAdmission, createBoundedProbeHandler, PROBE_REQUEST_LIMITS } from './probe-admission'
import type { Service } from './service'

afterEach(() => vi.useRealTimers())
function latch<T = void>() {
  let release!: (value: T) => void
  const promise = new Promise<T>((resolve) => { release = resolve })
  return { promise, release }
}

describe('bounded probe admission', () => {
  it('bounds active and FIFO waiting work and rejects excess without running it', async () => {
    const gate = new BoundedAdmission(2, 2)
    const locks = [latch(), latch(), latch(), latch()]
    const began: number[] = []
    const work = locks.map((lock, index) => gate.run(async () => { began.push(index); await lock.promise; return index }))
    const rejected = vi.fn(async () => 5)
    await expect(gate.run(rejected)).rejects.toMatchObject({ code: 'probe_overloaded', status: 503 })
    expect(rejected).not.toHaveBeenCalled()
    expect(began).toEqual([0, 1])
    locks[1].release()
    await work[1]
    expect(began).toEqual([0, 1, 2])
    locks[0].release()
    await work[0]
    expect(began).toEqual([0, 1, 2, 3])
    locks[2].release(); locks[3].release()
    expect(await Promise.all(work)).toEqual([0, 1, 2, 3])
    expect(gate.stats()).toMatchObject({ active: 0, queued: 0, max_active: 2, max_queued: 2, rejected: 1 })
  })

  it('releases a failed task but does not release an aborted active task early', async () => {
    const gate = new BoundedAdmission(1, 1)
    const lock = latch()
    const control = new AbortController()
    const running = gate.run(async () => { await lock.promise; throw Error('failed') }, control.signal)
    const observed = expect(running).rejects.toThrow('failed')
    control.abort()
    expect(gate.stats().active).toBe(1)
    const queued = gate.run(async () => 'next')
    expect(gate.stats().queued).toBe(1)
    lock.release()
    await observed
    expect(await queued).toBe('next')
    expect(gate.stats().active).toBe(0)
  })

  it('removes aborted queued work and enforces maximum queue wait', async () => {
    vi.useFakeTimers()
    const gate = new BoundedAdmission(1, 2, 10)
    const lock = latch()
    const running = gate.run(async () => lock.promise)
    const controller = new AbortController()
    const queued = gate.run(async () => 'never', controller.signal)
    const observed = expect(queued).rejects.toMatchObject({ status: 499 })
    controller.abort()
    await observed
    const expired = gate.run(async () => 'never')
    const timeout = expect(expired).rejects.toMatchObject({ code: 'probe_overloaded', status: 503 })
    await vi.advanceTimersByTimeAsync(10)
    await timeout
    expect(gate.stats()).toMatchObject({ active: 1, queued: 0 })
    lock.release(); await running
  })

  it('holds admission across cold loading and serializes real REST/MCP responses', async () => {
    const lock = latch<Service>()
    const load = vi.fn(() => lock.promise)
    const handler = createBoundedProbeHandler(load, new BoundedAdmission(1, 0))
    const first = handler.fetch(new Request('http://localhost/v1/catalog'))
    const excess = await handler.fetch(new Request('http://localhost/v1/catalog'))
    expect(excess.status).toBe(503)
    expect(excess.headers.get('retry-after')).toBe('1')
    lock.release({ catalog: async () => ({ corpus_version: 'a'.repeat(64), total: 0, papers: [], next_offset: null }) } as unknown as Service)
    expect((await first).status).toBe(200)
    const mcp = await handler.fetch(new Request('http://localhost/mcp', {
      method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream' },
      body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call',
        params: { name: 'list_papers', arguments: {} } }),
    }))
    expect(mcp.status).toBe(200)
    const wire = await mcp.text()
    const body = JSON.parse(wire.startsWith('event:') ? wire.split('\n').find((line) => line.startsWith('data: '))!.slice(6) : wire)
    expect(body.result.structuredContent.total).toBe(0)
    expect(JSON.parse(body.result.content[0].text).total).toBe(0)
    expect(handler.admission.stats().active).toBe(0)
  })

  it('bounds streamed request bodies before loading a service, including absent content-length', async () => {
    const load = vi.fn(async () => ({} as Service))
    const handler = createBoundedProbeHandler(load)
    const response = await handler.fetch(new Request('http://localhost/mcp', {
      method: 'POST', body: new Uint8Array(PROBE_REQUEST_LIMITS.request_bytes + 1),
    }))
    expect(response.status).toBe(413)
    expect(load).not.toHaveBeenCalled()
    expect(handler.admission.stats().active).toBe(0)
  })

  it('expires stalled uploads and frees every permit even when cancellation never settles', async () => {
    vi.useFakeTimers()
    const load = vi.fn(async () => ({ catalog: async () => ({
      corpus_version: 'a'.repeat(64), total: 0, papers: [], next_offset: null,
    }) } as unknown as Service))
    const handler = createBoundedProbeHandler(load)
    const cancellations = vi.fn(() => new Promise<void>(() => {}))
    const requests = Array.from({ length: 12 }, () => handler.fetch(new Request('http://localhost/mcp', {
      method: 'POST', body: new ReadableStream<Uint8Array>({ cancel: cancellations }), duplex: 'half',
    } as RequestInit)))
    expect(handler.admission.stats()).toMatchObject({ active: 4, queued: 8 })
    expect((await handler.fetch(new Request('http://localhost/v1/catalog'))).status).toBe(503)
    await vi.advanceTimersByTimeAsync(PROBE_REQUEST_LIMITS.body_read_ms)
    const responses = await Promise.all(requests)
    expect(responses.slice(0, 4).map((response) => response.status)).toEqual([408, 408, 408, 408])
    expect(responses.slice(4).every((response) => response.status === 503)).toBe(true)
    expect(cancellations).toHaveBeenCalledTimes(12)
    expect(load).not.toHaveBeenCalled()
    expect(handler.admission.stats()).toMatchObject({ active: 0, queued: 0 })
    expect((await handler.fetch(new Request('http://localhost/v1/catalog'))).status).toBe(200)
  })

  it('aborts an active body read without waiting for the source cancellation promise', async () => {
    const load = vi.fn(async () => ({} as Service))
    const handler = createBoundedProbeHandler(load, new BoundedAdmission(1, 0))
    const control = new AbortController()
    const cancel = vi.fn(() => new Promise<void>(() => {}))
    const pending = handler.fetch(new Request('http://localhost/mcp', {
      method: 'POST', signal: control.signal,
      body: new ReadableStream<Uint8Array>({ cancel }), duplex: 'half',
    } as RequestInit))
    expect(handler.admission.stats().active).toBe(1)
    control.abort()
    expect((await pending).status).toBe(499)
    expect(cancel).toHaveBeenCalledOnce()
    expect(load).not.toHaveBeenCalled()
    expect(handler.admission.stats().active).toBe(0)
  })

  it('uses one absolute body deadline despite a continuous trickle of chunks', async () => {
    vi.useFakeTimers()
    const load = vi.fn(async () => ({} as Service))
    const handler = createBoundedProbeHandler(load)
    let push!: ReadableStreamDefaultController<Uint8Array>
    const pending = handler.fetch(new Request('http://localhost/mcp', {
      method: 'POST', body: new ReadableStream<Uint8Array>({ start(controller) { push = controller } }),
      duplex: 'half',
    } as RequestInit))
    for (let i = 0; i < 4; i++) {
      await vi.advanceTimersByTimeAsync(1000)
      push.enqueue(new Uint8Array([32]))
    }
    await vi.advanceTimersByTimeAsync(1000)
    expect((await pending).status).toBe(408)
    expect(load).not.toHaveBeenCalled()
    expect(handler.admission.stats().active).toBe(0)
  })
})
