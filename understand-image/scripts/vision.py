#!/usr/bin/env python3
"""Image understanding via OpenAI Responses API compatible vision models."""

import sys
import base64
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    base_url="{BASE_URL}",
    api_key="{API_KEY}",
)

# Usage: python vision.py "IMAGE_PATH_OR_URL" "QUESTION"
image = sys.argv[1]
question = sys.argv[2]

if image.startswith(("http://", "https://")):
    image_content = {"type": "input_image", "image_url": image}
else:
    path = Path(image).expanduser().resolve()
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    suffix = path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif", "webp": "image/webp"}.get(suffix, "image/png")
    image_content = {"type": "input_image", "image_url": f"data:{mime};base64,{b64}"}

response = client.responses.create(
    model="{MODEL_NAME}",
    input=[{
        "role": "user",
        "content": [
            image_content,
            {"type": "input_text", "text": question},
        ],
    }],
)
print(response.output_text)
