# Tavily Cursor Plugin

Official Tavily plugin for Cursor. Adds web search, content extraction, website crawling, and AI-powered research capabilities.

## Skills

| Skill | Command | Description |
|-------|---------|-------------|
| **Search** | `/search` | Search the web using Tavily's LLM-optimized API. Returns relevant results with content snippets, scores, and metadata. |
| **Research** | `/research` | Comprehensive research on any topic with citations. Supports mini and pro models. |
| **Extract** | `/extract` | Extract clean content from specific URLs. Returns markdown/text from web pages. |
| **Crawl** | `/crawl` | Crawl websites to download documentation, knowledge bases, or web content as local markdown files. |
| **Best Practices** | `/tavily-best-practices` | Reference documentation for building production-ready Tavily integrations. |

## Authentication

**No manual setup required** — Uses OAuth via the Tavily MCP server.

> You must have an existing Tavily account. The OAuth flow only supports login — account creation is not available through this flow. [Sign up at tavily.com](https://tavily.com) first if you don't have an account.

On first run, the script will:
1. Check for existing tokens in `~/.mcp-auth/`
2. If none found, automatically open your browser for OAuth authentication

### Alternative: API Key

Get an API key at [https://tavily.com](https://tavily.com) and set it as an environment variable:

```
TAVILY_API_KEY=tvly-your-api-key-here
```


## License

MIT
