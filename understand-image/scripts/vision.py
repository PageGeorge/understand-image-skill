#!/usr/bin/env python3
"""Image understanding via OpenAI Responses API compatible vision models."""

import argparse
import base64
import sys
from pathlib import Path
from openai import OpenAI


def main():
    parser = argparse.ArgumentParser(description="Image understanding via vision models")
    parser.add_argument("image", help="Image file path or URL")
    parser.add_argument("question", help="Question about the image")
    parser.add_argument("--api-key", default="{API_KEY}", help="API key")
    parser.add_argument("--model", default="{MODEL_NAME}", help="Model name")
    args = parser.parse_args()

    # Determine if image is URL or local file
    image = args.image
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

    client = OpenAI(
        base_url="{BASE_URL}",
        api_key=args.api_key,
    )

    response = client.responses.create(
        model=args.model,
        input=[{
            "role": "user",
            "content": [
                image_content,
                {"type": "input_text", "text": args.question},
            ],
        }],
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
