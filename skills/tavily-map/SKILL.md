---
name: tavily-map
description: >
  Discover URLs on a known website without extracting page content. Use when
  the user wants the site structure, to find a specific page on a large site,
  or says "map the site", "list the pages", "what URLs are on", or "find the
  docs URL".
---

# Tavily Map

List URLs on a site so you can pick the right page before extracting or crawling.

## When

- You know the domain but not the exact page
- You need a sitemap-style view before a crawl
- Step 3: search → extract → **map** → crawl → research

Do not use this skill to read page content (extract) or to bulk-download a section (crawl). Map is faster and cheaper than crawl when you only need paths.

## How

- Start from the most specific base URL the user gave (for example `/docs`, not the marketing homepage).
- Use the URL list to choose extract vs crawl. Extract a handful of pages; crawl a section.
- Cite the URLs you recommend. Do not invent paths that were not returned.

## Execute

If `tavily_map` is callable (the name may be prefixed), call it. Do not install the CLI and do not run `tvly` for this. In a coding-agent terminal that is already using `tvly`, pass `--client-name "cursor plugin"` and take flags from `tvly map --help`. Never ask for an API key in chat.
