---
name: tavily-cli
description: >
  Install and authenticate the Tavily CLI (`tvly`) in a coding-agent terminal.
  Use only when the user asks to install tvly, run tvly login, or check CLI
  status, or when a terminal session has no callable Tavily MCP tools.
  Not for ordinary web search, extraction, mapping, crawling, or research.
compatibility: Requires tavily-cli 0.1.5 or newer and a Tavily API key from tavily.com.
allowed-tools: Bash(tvly *)
---

# Tavily CLI

Install and authenticate `tvly` for terminal coding agents. Capability choice (search, extract, map, crawl, research) lives in those skills. Arguments live in `tvly <command> --help`.

Do not use this skill on a native plugin host where Tavily MCP tools are callable.

## Install

Check first:

```bash
tvly --version
```

If missing:

```bash
curl -fsSL https://cli.tavily.com/install.sh | bash
```

Alternatives: `uv tool install tavily-cli` or `pip install tavily-cli`. Then confirm `tvly --version`. If the sandbox blocked the install, retry with sandbox disabled or have the user run the installer in their own terminal.

## Authenticate

```bash
tvly --status
tvly login
```

Prefer browser OAuth. Do not ask the user to paste an API key into chat. `tvly login --api-key` or `TAVILY_API_KEY` only when the user already has a key and chose that path.

## After install

Every `tvly` search, extract, map, crawl, and research call, including research status and poll, must include `--client-name "cursor plugin"`. Use `--json` for agentic output. Quote URLs. Exit codes: 0 success, 2 bad input, 3 auth, 4 API.

Return to the matching capability skill for when to search vs extract vs map vs crawl vs research.
