import { errorBody, DomainError, fail, parseBoundedInt, parseDirection, parseOffset } from './schemas'
import { embed } from './tokenize'
import { manual } from './manual'
import { openApiDocument } from './openapi'
import type { Service } from './service'

const JSON_HEADERS = {
  'content-type': 'application/json; charset=utf-8',
  'cache-control': 'no-store',
}

export function json(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), { status, headers: JSON_HEADERS })
}

export function allowedHost(host: string): boolean {
  return host === 'localhost' || host === '127.0.0.1' || host.endsWith('.workers.dev')
}

export function hostMatches(url: URL, hostHeader: string | null): boolean {
  if (!allowedHost(url.hostname)) {
    return false
  }
  if (!hostHeader) {
    return true
  }
  const headerHost = hostHeader.split(':')[0]
  return allowedHost(headerHost) && headerHost === url.hostname
}

export function requestOrigin(request: Request): string {
  const url = new URL(request.url)
  if (!hostMatches(url, request.headers.get('host'))) {
    fail('invalid_argument', 400, 'origin is not an allowed API host')
  }
  return url.origin
}

function firstParam(url: URL, name: string): string | null {
  return url.searchParams.get(name)
}

export async function handleRest(request: Request, service: Service): Promise<Response> {
  const url = new URL(request.url)
  try {
    if (request.method !== 'GET' && request.method !== 'HEAD') {
      return json(errorBody(new DomainError('invalid_argument', 405, 'method not allowed')), 405)
    }
    if (url.pathname === '/') {
      requestOrigin(request)
      return new Response(manual, {
        headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store' },
      })
    }
    if (url.pathname === '/openapi.json') {
      return json(openApiDocument(requestOrigin(request)))
    }
    if (url.pathname === '/health') {
      requestOrigin(request)
      return json(await service.health())
    }
    if (url.pathname === '/v1/paper') {
      requestOrigin(request)
      return json(await service.paper(firstParam(url, 'id') ?? ''))
    }
    if (url.pathname === '/v1/catalog') {
      requestOrigin(request)
      return json(await service.catalog({ q: firstParam(url, 'q') ?? '',
        section: firstParam(url, 'section') ?? undefined,
        offset: parseOffset(firstParam(url, 'offset')),
        limit: parseBoundedInt(firstParam(url, 'limit'), 12, 1, 24, 'limit'),
        version: firstParam(url, 'version') }))
    }
    if (url.pathname === '/v1/contents') {
      requestOrigin(request)
      return json(await service.contents(firstParam(url, 'id') ?? '', firstParam(url, 'version')))
    }
    if (url.pathname === '/v1/find') {
      requestOrigin(request)
      return json(await service.find({ id: firstParam(url, 'id') ?? '', q: firstParam(url, 'q') ?? '',
        offset: parseOffset(firstParam(url, 'offset')), version: firstParam(url, 'version') }))
    }
    if (url.pathname === '/v1/citations') {
      requestOrigin(request)
      return json(await service.citations({
        id: firstParam(url, 'id') ?? '',
        dir: parseDirection(firstParam(url, 'dir')),
        limit: parseBoundedInt(
          firstParam(url, 'limit'),
          embed.limits.citation_default,
          1,
          embed.limits.citation_max,
          'limit',
        ),
        cursor: firstParam(url, 'cursor'),
      }))
    }
    if (url.pathname === '/v1/traverse') {
      requestOrigin(request)
      return json(await service.traverse({
        id: firstParam(url, 'id') ?? '',
        dir: parseDirection(firstParam(url, 'dir')),
        hops: parseBoundedInt(
          firstParam(url, 'hops'),
          embed.limits.traverse_hops_default,
          1,
          embed.limits.traverse_hops_max,
          'hops',
        ),
        max_nodes: parseBoundedInt(firstParam(url, 'max_nodes'), 24, 2, 100, 'max_nodes'),
      }))
    }
    if (url.pathname === '/v1/content') {
      requestOrigin(request)
      return json(await service.content({
        id: firstParam(url, 'id') ?? '',
        offset: parseOffset(firstParam(url, 'offset')),
        version: firstParam(url, 'version'),
        length: parseBoundedInt(firstParam(url, 'length'), 6000, 1, 32000, 'length'),
      }))
    }
    if (url.pathname === '/v1/search') {
      requestOrigin(request)
      return json(await service.search({
        q: firstParam(url, 'q') ?? '',
        k: parseBoundedInt(
          firstParam(url, 'k'),
          embed.limits.search_k_default,
          1,
          embed.limits.search_k_max,
          'k',
        ),
        ip: request.headers.get('cf-connecting-ip') ?? 'unknown',
      }))
    }
    return json(errorBody(new DomainError('invalid_argument', 404, 'not found')), 404)
  } catch (error) {
    if (error instanceof DomainError) {
      const response = json(errorBody(error), error.status)
      if (error.status === 429) response.headers.set('retry-after', '60')
      return response
    }
    return json(errorBody(new DomainError('corpus_unavailable', 503, 'request failed')), 503)
  }
}
