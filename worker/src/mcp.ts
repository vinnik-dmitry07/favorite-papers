import { createMcpHandler } from 'agents/mcp/server'
import { McpServer } from '@modelcontextprotocol/server'
import { z } from 'zod'

import { DomainError, errorBody, parseBoundedInt, parseDirection, parseOffset } from './schemas'
import { embed } from './tokenize'
import { hostMatches, json } from './http'
import type { Service } from './service'

const readOnly = { readOnlyHint: true }

async function run(work: () => Promise<unknown>) {
  try {
    const body = await work()
    return { content: [{ type: 'text' as const, text: JSON.stringify(body) }] }
  } catch (error) {
    if (error instanceof DomainError) {
      return {
        isError: true as const,
        content: [{ type: 'text' as const, text: JSON.stringify(errorBody(error)) }],
      }
    }
    throw error
  }
}

function registerTools(server: McpServer, service: Service, ip: string) {
  server.registerTool(
    'search',
    {
      description: 'Search paper passages. Score is similarity, not a probability.',
      inputSchema: z.object({
        q: z.string(),
        k: z.number().optional(),
      }),
      annotations: readOnly,
    },
    async ({ q, k }) => run(() => service.search({
      q,
      k: parseBoundedInt(k, embed.limits.search_k_default, 1, embed.limits.search_k_max, 'k'),
      ip,
    })),
  )
  server.registerTool(
    'get_paper',
    {
      description: 'Paper card for a catalog id.',
      inputSchema: z.object({ id: z.string() }),
      annotations: readOnly,
    },
    async ({ id }) => run(() => service.paper(id)),
  )
  server.registerTool(
    'citations',
    {
      description: 'Paginated citation neighbors. dir is out, in, or both.',
      inputSchema: z.object({
        id: z.string(),
        dir: z.enum(['out', 'in', 'both']).optional(),
        limit: z.number().optional(),
        cursor: z.string().optional(),
      }),
      annotations: readOnly,
    },
    async ({ id, dir, limit, cursor }) => run(() => service.citations({
      id,
      dir: parseDirection(dir),
      limit: parseBoundedInt(limit, embed.limits.citation_default, 1, embed.limits.citation_max, 'limit'),
      cursor: cursor ?? null,
    })),
  )
  server.registerTool(
    'read_content',
    {
      description: 'Cleaned paper text. offset is a Unicode code-point index.',
      inputSchema: z.object({
        id: z.string(),
        offset: z.number().optional(),
        version: z.string().optional(),
      }),
      annotations: readOnly,
    },
    async ({ id, offset, version }) => run(() => service.content({
      id,
      offset: parseOffset(offset),
      version: version ?? null,
    })),
  )
  server.registerTool(
    'traverse',
    {
      description: 'Bounded BFS over citation neighbors. Returns a discovery tree.',
      inputSchema: z.object({
        id: z.string(),
        dir: z.enum(['out', 'in', 'both']).optional(),
        hops: z.number().optional(),
      }),
      annotations: readOnly,
    },
    async ({ id, dir, hops }) => run(() => service.traverse({
      id,
      dir: parseDirection(dir),
      hops: parseBoundedInt(hops, embed.limits.traverse_hops_default, 1, embed.limits.traverse_hops_max, 'hops'),
    })),
  )
}

function rejectedOrigin(): Response {
  return json(errorBody(new DomainError(
    'invalid_argument',
    400,
    'origin is not an allowed API host',
  )), 400)
}

export async function handleMcp(request: Request, service: Service): Promise<Response> {
  const url = new URL(request.url)
  if (!hostMatches(url, request.headers.get('host'))) {
    return rejectedOrigin()
  }
  const ip = request.headers.get('cf-connecting-ip') ?? 'unknown'
  const body = await request.arrayBuffer()
  if (body.byteLength > embed.limits.response_bytes_max) {
    return json(errorBody(new DomainError(
      'invalid_argument',
      400,
      'body exceeds the size cap',
    )), 400)
  }
  const headers = new Headers(request.headers)
  headers.delete('origin')
  if (!headers.get('host')) {
    headers.set('host', url.host)
  }
  const replay = new Request(request.url, {
    method: 'POST',
    headers,
    body,
  })
  const handler = createMcpHandler(() => {
    const server = new McpServer({ name: 'key-papers', version: '1' })
    registerTools(server, service, ip)
    return server
  }, {
    route: '/mcp',
    legacy: 'stateless',
    corsOptions: false,
  })
  return handler.fetch(replay)
}
