---
name: tavily-setup
description: Set up the Tavily plugin (install CLI and authenticate)
---

# Tavily Plugin Setup

## Step 1: Check if CLI is already installed

```bash
tvly --version
```

If this prints a version, skip to **Step 2: Authenticate**.

## Step 1b: Attempt installation

Try installing with the install script:

```bash
curl -fsSL https://cli.tavily.com/install.sh | bash
```

If that fails, try pip or uv:

```bash
pip install tavily-cli
```

or:

```bash
uv tool install tavily-cli
```

After either install method, verify it worked:

```bash
tvly --version
```

### If installation fails

Tell the user to re-run `/tavily-setup` with sandbox mode disabled. Installation requires network and filesystem access that Cursor's sandbox may block.

Alternatively, they can install manually in their own terminal:

```
curl -fsSL https://cli.tavily.com/install.sh | bash
```

or:

```
pip install tavily-cli
```

They may need to add `~/.local/bin` to PATH in their shell config (e.g. `~/.zshrc`). Ask them to re-run `/tavily-setup` once installed.

## Step 2: Authenticate

Check if already authenticated:

```bash
tvly --status
```

If not authenticated, run:

```bash
tvly login
```

This opens the browser for OAuth. Alternatively, the user can authenticate with an API key:

```bash
tvly login --api-key tvly-YOUR_KEY
```

Or set the environment variable:

```bash
export TAVILY_API_KEY=tvly-YOUR_KEY
```

## Step 3: Verify

```bash
tvly --status
```

Confirm the CLI is installed, authenticated, and ready to use.
