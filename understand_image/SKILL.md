---
name: understand_image
description: Analyze and understand images using vision models. Use when the user provides an image (file path or URL) and asks questions about it, wants to understand what's in an image, or needs image-based analysis.
allowed-tools: Bash(python3 *)
---

# Understand Image

Image understanding via OpenAI Responses API compatible vision models.

## Usage

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/vision.py "IMAGE_PATH_OR_URL" "QUESTION"
```

- `IMAGE_PATH_OR_URL`: local file path or HTTP(S) URL
- `QUESTION`: the question to ask about the image (decided by Claude based on user's intent)

## Notes

- Supports PNG, JPG, GIF, WebP
- Local files are auto-encoded to base64
- Determine the question based on what the user wants to know; be specific rather than generic
