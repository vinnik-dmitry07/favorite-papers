import { createMcpHandler } from 'agents/mcp/server'
import { McpServer } from '@modelcontextprotocol/server'

import { DomainError, errorBody } from './schemas'
import { inputs, outputs, descriptions } from './contracts'
import { embed } from './tokenize'
import { hostMatches, json } from './http'
import type { Service } from './service'

const readOnly = { readOnlyHint: true }

async function run(work: () => Promise<unknown>) {
  try {
    const body = await work()
    return { structuredContent: body as Record<string, unknown>,
      content: [{ type: 'text' as const, text: JSON.stringify(body) }] }
  } catch (error) {
    if (error instanceof DomainError) {
      return {
        isError: true as const,
        content: [{ type: 'text' as const, text: JSON.stringify(errorBody(error)) }],
      }
    }
    return { isError: true as const, content: [{ type: 'text' as const,
      text: JSON.stringify(errorBody(new DomainError('corpus_unavailable', 503, 'request failed'))) }] }
  }
}

function registerTools(server: McpServer, service: Service, ip: string) {
  server.registerTool('search', {
    description: descriptions.search, inputSchema: inputs.search,
    outputSchema: outputs.search, annotations: readOnly,
  }, async ({ query }) => run(() => service.researchSearch(query, ip)))
  server.registerTool('fetch', {
    description: descriptions.fetch, inputSchema: inputs.fetch,
    outputSchema: outputs.fetch, annotations: readOnly,
  }, async ({ id }) => run(() => service.fetchDocument(id)))
  server.registerTool('get_paper', {
    description: descriptions.paper, inputSchema: inputs.paper,
    outputSchema: outputs.paper, annotations: readOnly,
  }, async ({ id }) => run(() => service.paper(id)))
  server.registerTool('list_papers', {
    description: descriptions.catalog, inputSchema: inputs.catalog,
    outputSchema: outputs.catalog, annotations: readOnly,
  }, async (args) => run(() => service.catalog(args)))
  server.registerTool('citations', {
    description: descriptions.citations, inputSchema: inputs.citations,
    outputSchema: outputs.citations, annotations: readOnly,
  }, async (args) => run(() => service.citations({ ...args, cursor: args.cursor ?? null })))
  server.registerTool('traverse', {
    description: descriptions.traverse, inputSchema: inputs.traverse,
    outputSchema: outputs.traverse, annotations: readOnly,
  }, async (args) => run(() => service.traverse(args)))
  server.registerTool('read_content', {
    description: descriptions.content, inputSchema: inputs.content,
    outputSchema: outputs.content, annotations: readOnly,
  }, async (args) => run(() => service.content({ ...args, version: args.version ?? null })))
  server.registerTool('contents', {
    description: descriptions.contents, inputSchema: inputs.contents,
    outputSchema: outputs.contents, annotations: readOnly,
  }, async ({ id, version }) => run(() => service.contents(id, version)))
  server.registerTool('find_in_paper', {
    description: descriptions.find, inputSchema: inputs.find,
    outputSchema: outputs.find, annotations: readOnly,
  }, async (args) => run(() => service.find(args)))
  server.registerTool('search_passages', {
    description: descriptions.passages, inputSchema: inputs.passages,
    outputSchema: outputs.passages, annotations: readOnly,
  }, async (args) => run(() => service.search({ ...args, ip })))
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
