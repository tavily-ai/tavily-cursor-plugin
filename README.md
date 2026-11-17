# Tavily Cursor Plugin

> [!IMPORTANT]
> This plugin moved. The Tavily plugin for Cursor now lives in [tavily-ai/skills](https://github.com/tavily-ai/skills) and is available from the [Cursor Marketplace](https://cursor.com/marketplace/tavily). This repository is no longer maintained.

## Migrating

Use one of these two methods. Each method adds the Tavily skills and the hosted Tavily MCP server to Cursor.

### Cursor Marketplace

In a new Cursor Agent chat, enter this command:

```
/add-plugin tavily
```

You can also install Tavily from the [Cursor Marketplace](https://cursor.com/marketplace/tavily) page.

### Tavily CLI

In a terminal, run this command. It requires Node.js 20.1 or later.

```bash
npx @tavily/cli init --agent cursor
```

The command installs `tvly`, signs you in, and sets up Cursor. Restart Cursor after the setup completes.

### Local clones

If you work from a local clone of this repository, switch to the Marketplace plugin. This repository does not receive updates.

### What changed

The plugin in tavily-ai/skills has a different set of skills:

- One `tavily-search` skill covers search, extract, map, and crawl.
- The task skills are `tavily-research`, `tavily-entity`, `tavily-list`, and `tavily-monitor`.
- The `tavily-sdk` skill holds reference documents for developers who build Tavily integrations.
- The slash commands of this repository, such as `/search` and `/tavily-setup`, are not part of the new plugin.

For setup, authentication, and the full list of skills, see the [Cursor plugin section](https://github.com/tavily-ai/skills#cursor-plugin) of the tavily-ai/skills README. The plugin manifest is in [`.cursor-plugin/`](https://github.com/tavily-ai/skills/tree/main/.cursor-plugin).

## Links

- [tavily-ai/skills](https://github.com/tavily-ai/skills)
- [Tavily on the Cursor Marketplace](https://cursor.com/marketplace/tavily)
- [Tavily Documentation](https://docs.tavily.com)

## License

MIT
