# Tavily Cursor Plugin

Official Tavily plugin for the Cursor marketplace (including Grok Bot). Skills choose the capability. MCP provides the tools. The CLI is a terminal fallback.

## Features

| Capability | Skill | Command |
|-----------|-------|---------|
| Web Search | `tavily-search` | `/search` |
| Content Extraction | `tavily-extract` | `/extract` |
| URL Mapping | `tavily-map` | `/map` |
| Website Crawling | `tavily-crawl` | `/crawl` |
| Deep Research | `tavily-research` | `/research` |

Additional commands: `/tavily-setup`, `/tavily-status`, `/tavily-best-practices`

## Installation

1. Install the plugin from the marketplace (or see Local Development to test from source).
2. Connect the Tavily MCP server (OAuth). On a native host, that is the whole setup.
3. In a coding-agent terminal only, run `/tavily-setup` if you need `tvly`.

### Manual CLI Setup (terminal only)

```bash
curl -fsSL https://cli.tavily.com/install.sh | bash
tvly login
```

Or via pip:

```bash
pip install tavily-cli
tvly login
```

Or via uv:

```bash
uv tool install tavily-cli
tvly login
```

## Quick Start

Search the web:

```
/search latest developments in AI chip manufacturing
```

Extract content from a URL:

```
/extract https://docs.example.com/api
```

Discover URLs on a site:

```
/map https://docs.example.com
```

Crawl documentation:

```
/crawl https://docs.example.com
```

Deep research:

```
/research competitive landscape of AI code assistants
```

## Plugin Structure

```
.cursor-plugin/plugin.json    Plugin manifest
mcp.json                      Hosted Tavily MCP server
skills/                       Capability skills (when to search, extract, map, crawl, research)
commands/                     Slash commands
```

## Local Development

1. Clone the repository
2. Open the folder in Cursor
3. Skills are auto-discovered from `skills/`
4. For commands, symlink into `.cursor/`:
   ```bash
   ln -s ../commands .cursor/commands
   ```
5. Type `/` — the commands should now appear alongside the skills.
6. Connect MCP, or run `/tavily-setup` in a terminal if you need the CLI.

## License

MIT
