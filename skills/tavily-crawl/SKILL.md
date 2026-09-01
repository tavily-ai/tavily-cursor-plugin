---
name: tavily-crawl
description: >
  Collect content from many pages on the same site. Use when the user wants to
  crawl, download docs, extract a whole section such as /docs, bulk-extract
  pages, or says "get all the pages" or "extract everything under".
---

# Tavily Crawl

Gather content from a site section, not from the open web.

## When

- You need many pages under one site (docs, API reference, a path prefix)
- Step 4: search → extract → map → **crawl** → research

Do not use this skill for a single known URL (extract), for URL discovery only (map), or for a cited multi-source report across the web (research).

## How

- Map first when the target section is unclear.
- Stay narrow: limit depth and page count; constrain to the paths you need.
- For answering a question, prefer instruction-guided, chunked crawls over dumping every page into context.
- For saving a docs tree onto disk, do that only in a terminal with a real filesystem. On a connector host, return the crawled content instead.
- Cite the pages you used. Always cap the crawl so it cannot run away.

## Execute

If `tavily_crawl` is callable (the name may be prefixed), call it. Do not install the CLI and do not run `tvly` for this. In a coding-agent terminal that is already using `tvly`, pass `--client-name "cursor plugin"` and take flags from `tvly crawl --help`. Never ask for an API key in chat.
