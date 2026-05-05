#!/usr/bin/env python3
"""Image understanding via OpenAI Responses API compatible vision models."""

from __future__ import annotations

import argparse
import base64
import sys
from pathlib import Path

API_KEY = "{API_KEY}"
BASE_URL = "{BASE_URL}"
MODEL_NAME = "{MODEL_NAME}"

SUPPORTED_MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
}


class ConfigError(RuntimeError):
    """Raised when the local skill copy has not been configured."""


class UserInputError(RuntimeError):
    """Raised when the image argument cannot be used."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ask a vision model a question about an image."
    )
    parser.add_argument("image", help="Local image file path or HTTP(S) image URL")
    parser.add_argument("question", help="Question to ask about the image")
    return parser.parse_args()


def validate_config() -> None:
    missing = []
    if not API_KEY.strip() or API_KEY.strip() == "{API_KEY}":
        missing.append("API_KEY")
    if not BASE_URL.strip() or BASE_URL.strip() == "{BASE_URL}":
        missing.append("BASE_URL")
    if not MODEL_NAME.strip() or MODEL_NAME.strip() == "{MODEL_NAME}":
        missing.append("MODEL_NAME")

    if missing:
        raise ConfigError(
            "missing configuration for "
            + ", ".join(missing)
            + "; replace {API_KEY}, {BASE_URL}, and {MODEL_NAME} in scripts/vision.py"
        )


def guess_mime_type(path: Path) -> str:
    mime_type = SUPPORTED_MIME_TYPES.get(path.suffix.lower())
    if not mime_type:
        supported = ", ".join(sorted(SUPPORTED_MIME_TYPES))
        raise UserInputError(
            f"unsupported image format '{path.suffix or '(none)'}'; supported: {supported}"
        )
    return mime_type


def build_image_content(image: str) -> dict:
    if image.startswith(("http://", "https://")):
        return {"type": "input_image", "image_url": image}

    if "://" in image:
        raise UserInputError("only local image paths and HTTP(S) image URLs are supported")

    path = Path(image).expanduser()
    if not path.exists():
        raise UserInputError(f"file not found: {path}")
    if not path.is_file():
        raise UserInputError(f"not a file: {path}")

    resolved = path.resolve()
    mime_type = guess_mime_type(resolved)
    encoded = base64.b64encode(resolved.read_bytes()).decode("ascii")
    return {
        "type": "input_image",
        "image_url": f"data:{mime_type};base64,{encoded}",
    }


def ask_model(image_content: dict, question: str) -> str:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ConfigError(
            "Python package 'openai' is not installed; install it with "
            "`python3 -m pip install openai` or `python -m pip install openai`"
        ) from exc

    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY,
    )
    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {
                "role": "user",
                "content": [
                    image_content,
                    {"type": "input_text", "text": question},
                ],
            }
        ],
    )
    answer = getattr(response, "output_text", "").strip()
    if not answer:
        raise RuntimeError("the model returned an empty response")
    return answer


def main() -> int:
    args = parse_args()
    try:
        validate_config()
        image_content = build_image_content(args.image)
        print(ask_model(image_content, args.question))
        return 0
    except (ConfigError, UserInputError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Error: interrupted", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error: vision request failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
