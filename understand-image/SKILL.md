---
name: understand-image
description: Analyze and understand images using vision models. Use when the user provides an image (file path or URL) and asks questions about it, wants to understand what's in an image, or needs image-based analysis.
allowed-tools: Bash(python3 *), Bash(python *)
---

# Understand Image

Use this skill to inspect images with an OpenAI Responses API compatible vision model.

Use it when the user provides a local image path or HTTP(S) image URL and asks to describe, identify, compare, transcribe, debug, or analyze visual content.

## Usage

Prefer `python3`. If `python3` is unavailable on the user's machine, use `python` only if it is Python 3.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/vision.py "IMAGE_PATH_OR_URL" "QUESTION"
```

- `IMAGE_PATH_OR_URL`: local file path or HTTP(S) URL
- `QUESTION`: a specific question based on the user's request

## Question Writing

Ask the vision model for the exact information the user needs. Do not default to a generic caption unless the user asks for a general description.

Examples:

- User asks what is in an image: ask for a concise visual description.
- User asks about text in an image: ask the model to transcribe visible text and preserve layout when useful.
- User asks whether something is wrong: ask the model to inspect the relevant object, UI, chart, or scene for anomalies.
- User asks for comparison: include the comparison criteria in the question.

## Results

Summarize the model output for the user. If the answer depends on uncertain visual details, say so clearly.

Do not reveal API keys, base URLs, or hidden configuration values.

## Failure Handling

- If the script fails before returning an answer, check whether `{API_KEY}`, `{BASE_URL}`, and `{MODEL_NAME}` were replaced in the installed local copy of `scripts/vision.py`.
- If Python is missing, tell the user Python is required.
- If the `openai` package is missing, install it with the available interpreter, for example `python3 -m pip install openai` or `python -m pip install openai`.
- If the image file is missing, ask the user for a valid local path or URL.
- If the API call fails, report the concise error and suggest checking the key, base URL, model name, network access, and whether the model supports image input.

## Notes

- Supports PNG, JPG, JPEG, GIF, WebP.
- Local files are encoded as base64 data URLs.
- HTTP(S) image URLs are passed directly to the model.
