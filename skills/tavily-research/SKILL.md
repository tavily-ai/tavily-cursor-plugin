---
name: tavily-research
description: >
  Produce cited multi-source research. Use when the user wants a deep report,
  comparison, market analysis, or literature review, or says "research",
  "investigate", "analyze in depth", "compare X vs Y", or "what does the
  market look like for". For a quick fact, use tavily-search instead.
---

# Tavily Research

Synthesize a grounded report from multiple sources, with citations. This is slower than search.

## When

- The user needs comparison, market context, or a literature-style brief
- Quick search snippets are not enough
- Step 5: search → extract → map → crawl → **research**

Do not use this skill for a simple lookup (search) or for pulling one site’s docs (crawl).

## How

- Clarify scope, freshness, geography, and output shape only when they are ambiguous.
- Wait for the research run to finish. Preserve source URLs and distinguish sourced facts from your analysis.
- Prefer research when the deliverable is the report. Prefer search when the user wants a short answer now.

## Execute

If `tavily_research` is callable (the name may be prefixed), call it. Do not install the CLI and do not run `tvly` for this. In a coding-agent terminal that is already using `tvly`, pass `--client-name "cursor plugin"` and take flags from `tvly research --help`. Never ask for an API key in chat.
