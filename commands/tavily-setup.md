---
name: tavily-setup
description: Set up the Tavily plugin (connect MCP or install CLI and authenticate)
---

# Tavily Plugin Setup

Pick one primary surface. Prefer MCP when Tavily tools are callable.

## Native plugin host (Cursor desktop, Grok Bot, connectors)

1. If a Tavily MCP search tool is callable, run one live search for `Tavily Search API`. If it succeeds, setup is complete. Do not install the CLI.
2. If MCP tools are present but not authenticated, complete the host's OAuth flow for `https://mcp.tavily.com/mcp`. Never ask the user to paste an API key into chat.
3. If this host does not use the Tavily CLI, stop after MCP is callable.

## Terminal coding agent (Cursor CLI, Claude Code, Codex CLI)

Use the **tavily-cli** skill to install and authenticate `tvly`, then run one live `tvly search "Tavily Search API" --client-name "cursor plugin" --max-results 1 --json`. A successful CLI request does not prove MCP is connected.
