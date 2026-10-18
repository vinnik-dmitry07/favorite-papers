export const manual = `Key papers agent API

This API reads one citation catalog. An edge means the source paper cites the target. cites on a node is the in-degree. refs is the out-degree. Evidence is id, title, or url. Ids keep their catalog spelling (arxiv:, doi:, openreview:, acl:, url:) and their case. They are query parameters, not URL path segments.

Papers with no cleaned text stay on the graph and return available: false. Search returns passages, not one row per paper. Scores are similarity, not probabilities. Offsets are Unicode code points.

Examples
  GET /v1/paper?id=arxiv:1706.03762
  GET /v1/citations?id=arxiv:1706.03762&dir=out&limit=12
  GET /v1/traverse?id=arxiv:1706.03762&dir=out&hops=1
  GET /v1/content?id=arxiv:1706.03762&offset=0&version=<corpus_version>
  GET /v1/search?q=attention&k=5
  GET /health
  GET /openapi.json
  POST /mcp

Import /openapi.json as a Custom GPT Action with authentication None. Add POST /mcp as a remote MCP connector in a client that supports it, including ChatGPT where the account allows read or fetch connectors. A public URL does not register the tool by itself.
`
