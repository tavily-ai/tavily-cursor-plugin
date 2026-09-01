---
name: tavily-status
description: "Check Tavily MCP or CLI readiness. Usage: /tavily-status"
---

# Check Tavily Status

Report the live surface only. Prefer MCP when Tavily tools are callable.

If a Tavily MCP search tool is callable, treat MCP as ready. Optionally run one live search for `Tavily Search API`. Do not install the CLI.

If this is a terminal coding agent without callable MCP, use the **tavily-cli** skill and `tvly --status`.

If neither surface is ready, tell the user to run `/tavily-setup`.
