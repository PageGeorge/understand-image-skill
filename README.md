# Understand Image

A Claude Code skill that enables image understanding via OpenAI Responses API compatible vision models.

## API

Uses the OpenAI Responses API format (`client.responses.create`), compatible with any provider that exposes this endpoint.

## Configuration

Before using, replace the placeholders in `understand_image/scripts/vision.py`:

| Placeholder | Description |
|---|---|
| `{API_KEY}` | Your API key |
| `{BASE_URL}` | API endpoint (e.g. `https://ark.cn-beijing.volces.com/api/v3`) |
| `{MODEL_NAME}` | Model identifier (e.g. `doubao-seed-2-0-pro-260215`) |

## Installation

Copy the `understand_image` folder to your Claude Code skills directory:

```bash
# Personal (all projects)
cp -r understand_image ~/.claude/skills/

# Or project-specific
cp -r understand_image .claude/skills/
```

Then restart Claude Code. The skill will auto-trigger when you provide an image and ask a question about it, or you can invoke it manually with `/understand_image`.

## Usage

Provide an image (local file path or URL) and ask anything about it. Claude will determine the appropriate question to send to the vision model.

## Supported Formats

PNG, JPG, GIF, WebP.
