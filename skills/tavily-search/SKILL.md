---
name: tavily-search
description: >
  Search the web for current sources and snippets. Use when the user wants to
  search, look up, find articles, get recent news, or discover sources, and
  does not already have a URL. Triggers: "search for", "look up", "find me",
  "what's the latest on", "find articles about".
---

# Tavily Search

Find pages and current information when you do not already have a URL.

## When

- The user needs information on a topic and has not supplied a URL
- First step: **search** → extract → map → crawl → research

Do not use this skill when the user already has URLs (extract), needs every page in a site section (crawl), needs to locate pages on a known site (map), or wants a cited multi-source report (research).

## How

- Write short search queries, not prompts — keep each under 400 characters. Split multi-part questions into separate queries.
- Apply domain, topic, or date constraints when the user specified them.
- Prefer primary sources for factual or technical claims. Cross-check consequential facts.
- Cite source URLs. Synthesize; do not paste raw result dumps. Do not request full page HTML for every hit; if snippets are thin, extract the best URLs instead.

If snippets are not enough, extract the best URLs. If the user needs a full cited briefing, switch to research.

## Execute

If `tavily_search` is callable (the name may be prefixed), call it. Do not install the CLI and do not run `tvly` for this. In a coding-agent terminal that is already using `tvly`, pass `--client-name "cursor plugin"` and take flags from `tvly search --help`. Never ask for an API key in chat.
