import vocabText from '../tokenizer/vocab.txt'

import type { CorpusStore } from './corpus'
import { handleRest } from './http'
import { handleMcp } from './mcp'
import { createService, type Service } from './service'
import { embed, WordPieceTokenizer } from './tokenize'

const tokenizer = new WordPieceTokenizer(vocabText)

export interface Env {
  AI: {
    run(model: string, input: { text: string[], pooling: string }): Promise<{ data?: number[] | number[][] }>
  }
  VECTORIZE: {
    query(vector: number[], options: {
      namespace: string
      topK: number
      returnMetadata: 'all'
    }): Promise<{ matches?: { id: string, score: number, metadata?: Record<string, unknown> }[] }>
  }
  CORPUS: {
    get(key: string): Promise<{ json(): Promise<unknown> } | null>
  }
  SEARCH_LIMIT: {
    limit(options: { key: string }): Promise<{ success: boolean }>
  }
  SEARCH_ENABLED?: string
}

function storeFromEnv(env: Env): CorpusStore {
  return {
    now: () => Date.now(),
    async getJson(key: string) {
      const object = await env.CORPUS.get(key)
      if (!object) {
        return null
      }
      return object.json()
    },
    async embed(text: string) {
      const result = await env.AI.run(embed.model, {
        text: [text],
        pooling: embed.pooling,
      })
      const data = result?.data
      if (Array.isArray(data) && typeof data[0] === 'number') {
        return data as number[]
      }
      if (Array.isArray(data) && Array.isArray(data[0])) {
        return data[0]
      }
      throw new Error('embedding response was empty')
    },
    async query(namespace, vector, topK) {
      const result = await env.VECTORIZE.query(vector, {
        namespace,
        topK,
        returnMetadata: 'all',
      })
      return (result.matches ?? []).map((hit) => ({
        id: hit.id,
        score: hit.score,
      }))
    },
    async rateLimit(key: string) {
      const result = await env.SEARCH_LIMIT.limit({ key })
      return result.success
    },
  }
}

let appService: { enabled: string, service: Service } | null = null

export function createApp(service: Service) {
  return {
    async fetch(request: Request): Promise<Response> {
      const url = new URL(request.url)
      if (url.pathname === '/mcp') {
        if (request.method !== 'POST') {
          return new Response(null, { status: 405, headers: { allow: 'POST' } })
        }
        return handleMcp(request, service)
      }
      return handleRest(request, service)
    },
  }
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const enabled = env.SEARCH_ENABLED ?? '1'
    if (!appService || appService.enabled !== enabled) {
      appService = {
        enabled,
        service: createService(storeFromEnv(env), tokenizer, {
          searchEnabled: enabled !== '0' && embed.search_enabled,
        }),
      }
    }
    return createApp(appService.service).fetch(request)
  },
}
