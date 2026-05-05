# Understand Image

A Claude Code skill that lets an agent inspect and answer questions about images using an OpenAI Responses API compatible vision model.

This repository is designed to be installed by an agent. As a human user, you usually only need to give this repository URL to your agent and ask it to install the skill:

```text
https://github.com/PageGeorge/understand-image-skill
```

During installation, the agent should ask you for the required API key, base URL, and model name, then write those values into the local copy of the skill.

## What It Does

- Accepts a local image path or HTTP(S) image URL.
- Sends the image and a natural language question to a vision model.
- Returns the model's answer to the agent.
- Works with providers that expose an OpenAI Responses API compatible endpoint.

Supported image formats: PNG, JPG, JPEG, GIF, WebP.

## For Users

Ask your agent to install this skill from the repository URL above.

The agent will need three values from you:

| Value | Description |
|---|---|
| API key | Your provider API key |
| Base URL | The OpenAI-compatible API endpoint, for example `https://ark.cn-beijing.volces.com/api/v3` |
| Model name | A vision-capable model identifier, for example `doubao-seed-2-0-pro-260215` |

After installation, provide an image and ask a question about it. The skill should trigger automatically when the agent sees an image path or URL and the task requires visual understanding.

## For Agents

Install the `understand-image` folder into the user's Claude Code skills directory.

Personal installation:

```bash
cp -r understand-image ~/.claude/skills/
```

Project-specific installation:

```bash
mkdir -p .claude/skills
cp -r understand-image .claude/skills/
```

Install the Python dependency if it is not already available:

```bash
python3 -m pip install openai
```

If the machine only provides `python` and it points to Python 3, use `python` instead of `python3`.

Then configure the local installed copy by replacing these placeholders in `understand-image/scripts/vision.py`:

| Placeholder | Replace with |
|---|---|
| `{API_KEY}` | The user's API key |
| `{BASE_URL}` | The user's OpenAI-compatible base URL |
| `{MODEL_NAME}` | The user's vision model name |

Do not commit or publish the user's configured `vision.py` after inserting credentials.

Restart Claude Code after installation so the skill can be discovered.

## Verification

After configuration, run:

```bash
python3 ~/.claude/skills/understand-image/scripts/vision.py "IMAGE_PATH_OR_URL" "Describe this image."
```

For a project-specific installation, adjust the path:

```bash
python3 .claude/skills/understand-image/scripts/vision.py "IMAGE_PATH_OR_URL" "Describe this image."
```

If `python3` is unavailable, use `python` only after confirming it is Python 3.

If the script returns a visual description, the skill is ready.

## How It Works

The skill exposes a small Python helper script at:

```text
understand-image/scripts/vision.py
```

For local files, the script base64-encodes the image and sends it as a data URL. For HTTP(S) URLs, it passes the image URL directly to the model. The request uses `client.responses.create(...)` from the OpenAI Python SDK.

## Safety Notes

- Configure credentials only in the user's local installed copy.
- Do not push configured API keys back to GitHub.
- If the model fails, confirm that the selected model supports image input through the Responses API.
