import { createProbeApp, type ProbeEnv } from './static-search-probe'
import { validProbeToken } from './probe-auth'

export interface DoProbeEnv extends ProbeEnv {
  SEARCH_PROBE: Pick<DurableObjectNamespace, 'idFromName' | 'get'>
  PROBE_TOKEN: string
  PROBE_EXPIRES_AT: string
}

// This identity is server controlled. Query text, paper IDs and versions never
// create namespaces or objects. A fresh deployment owns its own namespace.
export const PROBE_OBJECT_NAME = 'synthetic-corpus'
const SAFE_LABEL = /^[a-zA-Z0-9_.:-]{1,128}$/

function closed(status: number, error: string): Response {
  return new Response(JSON.stringify({ error }), {
    status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' },
  })
}

export class StaticSearchProbe {
  private readonly app: ReturnType<typeof createProbeApp>

  constructor(state: DurableObjectState, private readonly env: DoProbeEnv) {
    this.app = createProbeApp({
      fixedVariant: 'wasm-json16', runtimeRole: 'durable_object', objectId: state.id.toString(),
    })
  }

  fetch(request: Request): Promise<Response> {
    return this.app.fetch(request, this.env)
  }
}

/** Forward the body unchanged; tokenization, index and response assembly live in the DO. */
export function createDoProbeGateway() {
  let bootId: string | undefined
  return {
    async fetch(request: Request, env: DoProbeEnv): Promise<Response> {
      const expiresAt = Date.parse(env.PROBE_EXPIRES_AT)
      if (!Number.isFinite(expiresAt) || Date.now() >= expiresAt) return closed(503, 'probe_expired')
      if (!validProbeToken(env.PROBE_TOKEN, request.headers.get('x-probe-token'))) return closed(403, 'probe_forbidden')
      const suppliedMarker = request.headers.get('x-probe-marker')
      const runId = request.headers.get('x-probe-run-id')
      if ((suppliedMarker !== null && !SAFE_LABEL.test(suppliedMarker))
          || (runId !== null && !SAFE_LABEL.test(runId))) return closed(400, 'invalid_probe_marker')
      const marker = suppliedMarker ?? crypto.randomUUID()
      bootId ??= crypto.randomUUID()
      console.log({ kind: 'static_do_probe', runtime_role: 'gateway', probe_marker: marker,
        run_id: runId, boot_id: bootId })
      const headers = new Headers(request.headers)
      // Secrets are only checked at ingress and are never forwarded or logged.
      headers.delete('x-probe-token')
      headers.set('x-probe-marker', marker)
      const forwarded = new Request(request, { headers })
      const id = env.SEARCH_PROBE.idFromName(PROBE_OBJECT_NAME)
      return env.SEARCH_PROBE.get(id).fetch(forwarded)
    },
  }
}

export default createDoProbeGateway()
