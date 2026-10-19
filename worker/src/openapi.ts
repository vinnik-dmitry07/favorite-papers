import { z } from 'zod'
import { descriptions, inputs, outputs } from './contracts'

const errorSchema = {
  type: 'object', required: ['error'],
  properties: { error: {
    type: 'object', required: ['code', 'message', 'details'],
    properties: { code: { type: 'string' }, message: { type: 'string' },
      details: { type: 'object', additionalProperties: true } },
  } },
}
const errors = Object.fromEntries([
  ['400', 'Invalid argument, offset, or query'], ['404', 'Unknown catalog id'],
  ['409', 'Corpus changed: restart search or pagination'],
  ['429', 'Uncached semantic search rate limit. Retry-After: 60'],
  ['503', 'Corpus, configuration, or semantic service unavailable'],
].map(([code, description]) => [code, { description,
  content: { 'application/json': { schema: errorSchema } } }]))

type Operation = Exclude<keyof typeof inputs, 'search' | 'fetch'>
function operation(name: Operation, operationId: string) {
  const input = z.toJSONSchema(inputs[name], { io: 'input' })
  const schema = z.toJSONSchema(outputs[name])
  const required = (input.required ?? []) as string[]
  return { get: {
    operationId, summary: descriptions[name], description: descriptions[name], security: [],
    parameters: Object.entries(input.properties ?? {}).map(([key, value]) => ({
      name: key, in: 'query', required: required.includes(key), schema: value,
      ...(key === 'id' ? { example: 'arxiv:2402.03300' } : {}),
    })),
    responses: { '200': { description: 'Successful read',
      content: { 'application/json': { schema } } }, ...errors },
  } }
}

export function openApiDocument(origin: string) {
  return {
    openapi: '3.1.0',
    info: { title: 'Key papers agent API', version: '1.1',
      description: 'Read a bounded citation catalog. Resolve titles with getCatalog before using IDs. '
        + 'All offsets are Unicode code points. in means cited by; out means cites. '
        + 'Source URLs and static paper pages are citable. Authentication is none.' },
    servers: [{ url: origin }], security: [],
    paths: {
      '/': { get: { operationId: 'getManual', summary: 'Agent quickstart and examples',
        responses: { '200': { description: 'Plain text manual',
          content: { 'text/plain': { schema: { type: 'string' } } } } } } },
      '/health': { get: { operationId: 'getHealth', summary: 'Release health without embedding a query',
        responses: { '200': { description: 'Inspect status, not only HTTP status',
          content: { 'application/json': { schema: { type: 'object',
            required: ['status', 'reader_schema'], properties: {
              status: { type: 'string', enum: ['ready', 'degraded', 'unavailable'] },
              reader_schema: { type: 'integer' }, release_id: { type: ['string', 'null'] },
              search_enabled: { type: 'boolean' },
            }, additionalProperties: true } } } } } } },
      '/v1/catalog': operation('catalog', 'getCatalog'),
      '/v1/paper': operation('paper', 'getPaper'),
      '/v1/citations': operation('citations', 'getCitations'),
      '/v1/traverse': operation('traverse', 'traverse'),
      '/v1/content': operation('content', 'readContent'),
      '/v1/contents': operation('contents', 'getContents'),
      '/v1/find': operation('find', 'findInPaper'),
      '/v1/search': operation('passages', 'searchPassages'),
    },
  }
}
