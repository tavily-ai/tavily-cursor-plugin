---
name: tavily-extract
description: >
  Extract clean content from known URLs. Use when the user supplies one or more
  URLs and wants the page text, says "extract", "grab the content from",
  "pull the text from", "get the page at", or "read this webpage".
---

# Tavily Extract

Pull clean page content from URLs you already have.

## When

- The user provided URLs, or search already found the right pages
- Step 2: search → **extract** → map → crawl → research

Do not use this skill to discover pages (search or map) or to bulk-collect a whole site section (crawl).

## How

- Extract only the URLs you need, at most 20 per call. Batch larger lists.
- Prefer query-focused extraction on long docs instead of entire pages.
- Retry with a deeper extract when the page is JavaScript-heavy, protected, or table-heavy and the first pass is empty or thin.
- Skip extract when search results already include the content you need.
- Cite URLs. Summarize for the user; do not dump full page text unless they asked for it.

If many pages on one site are required, crawl. If you still need to find the right path on a large site, map first.

## Execute

If `tavily_extract` is callable (the name may be prefixed), call it. Do not install the CLI and do not run `tvly` for this. In a coding-agent terminal that is already using `tvly`, pass `--client-name "cursor plugin"` and take flags from `tvly extract --help`. Never ask for an API key in chat.
