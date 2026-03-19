# Tavily Cursor Plugin

Official Tavily plugin for Cursor. Adds web search, content extraction, website crawling, URL discovery, and AI-powered research capabilities — powered by the `tvly` CLI.

## Features

| Capability | Skill | Command |
|-----------|-------|---------|
| Web Search | `tavily-search` | `/search` |
| Content Extraction | `tavily-extract` | `/extract` |
| Website Crawling | `tavily-crawl` | `/crawl` |
| URL Mapping | `tavily-map` | `/map` |
| Deep Research | `tavily-research` | `/research` |

Additional commands: `/tavily-setup`, `/tavily-status`, `/tavily-best-practices`

## Installation

1. Install the plugin in Cursor from the marketplace (or see Local Development to test from source).
2. Run `/tavily-setup` to install `tvly` CLI and authenticate.

### Manual CLI Setup

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

Crawl documentation:

```
/crawl https://docs.example.com
```

Discover URLs on a site:

```
/map https://docs.example.com
```

Deep research:

```
/research competitive landscape of AI code assistants
```

## Plugin Structure

```
.cursor-plugin/plugin.json    Plugin manifest
skills/                        7 skills (auto-discovered)
commands/                      8 slash commands
rules/                         Citation standards rule
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
6. Run `/tavily-setup` to confirm the CLI is installed and authenticated.

## License

MIT
