import { embed } from './tokenize'

const limits = embed.limits

const errorSchema = {
  type: 'object',
  required: ['error'],
  properties: {
    error: {
      type: 'object',
      required: ['code', 'message', 'details'],
      properties: {
        code: { type: 'string' },
        message: { type: 'string' },
        details: { type: 'object' },
      },
    },
  },
}

const errorResponses = {
  '400': { description: 'Invalid argument, cursor, offset, or query', content: { 'application/json': { schema: errorSchema } } },
  '404': { description: 'Unknown catalog id', content: { 'application/json': { schema: errorSchema } } },
  '409': { description: 'Corpus version conflict', content: { 'application/json': { schema: errorSchema } } },
  '429': { description: 'Search rate limit', content: { 'application/json': { schema: errorSchema } } },
  '503': { description: 'Corpus or configuration is not usable', content: { 'application/json': { schema: errorSchema } } },
}

function op(operationId: string, summary: string, parameters: unknown[]) {
  return {
    get: {
      operationId,
      summary,
      security: [],
      parameters,
      responses: {
        '200': { description: summary },
        ...errorResponses,
      },
    },
  }
}

const idParam = {
  name: 'id',
  in: 'query',
  required: true,
  schema: { type: 'string', maxLength: limits.id_bytes_max },
  description: 'Catalog id. Case-sensitive. URL-encode once.',
}

export function openApiDocument(origin: string) {
  return {
    openapi: '3.1.0',
    info: {
      title: 'Key papers agent API',
      version: '1',
      description: 'Read the citation catalog, paper text, and passage search. Authentication is none.',
    },
    servers: [{ url: origin }],
    security: [],
    paths: {
      '/': op('getManual', 'API manual', []),
      '/health': op('getHealth', 'Release health without embeddings', []),
      '/v1/paper': op('getPaper', 'Paper card', [idParam]),
      '/v1/citations': op('getCitations', 'Paginated citation neighbors', [
        idParam,
        { name: 'dir', in: 'query', schema: { type: 'string', enum: ['out', 'in', 'both'], default: 'out' } },
        { name: 'limit', in: 'query', schema: { type: 'integer', minimum: 1, maximum: limits.citation_max, default: limits.citation_default } },
        { name: 'cursor', in: 'query', schema: { type: 'string' } },
      ]),
      '/v1/traverse': op('traverse', 'Bounded citation BFS', [
        idParam,
        { name: 'dir', in: 'query', schema: { type: 'string', enum: ['out', 'in', 'both'], default: 'out' } },
        { name: 'hops', in: 'query', schema: { type: 'integer', minimum: 1, maximum: limits.traverse_hops_max, default: limits.traverse_hops_default } },
      ]),
      '/v1/content': op('readContent', 'Cleaned paper text', [
        idParam,
        { name: 'offset', in: 'query', schema: { type: 'integer', minimum: 0, default: 0 } },
        { name: 'version', in: 'query', schema: { type: 'string' } },
      ]),
      '/v1/search': op('searchPassages', 'Semantic passage search', [
        { name: 'q', in: 'query', required: true, schema: { type: 'string' } },
        { name: 'k', in: 'query', schema: { type: 'integer', minimum: 1, maximum: limits.search_k_max, default: limits.search_k_default } },
      ]),
    },
  }
}
