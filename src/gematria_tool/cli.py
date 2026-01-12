"""Command-line interface for gematria tool."""

from __future__ import annotations

import argparse

from gematria_tool.core import gematria


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Calculate gematria/isopsephy values for Hebrew or Greek text."
        )
    )
    parser.add_argument("text", help="Text to evaluate.")
    parser.add_argument(
        "-l",
        "--language",
        default="hebrew",
        choices=["hebrew", "greek"],
        help="Language mapping to use (default: hebrew).",
    )
    parser.add_argument(
        "--lenient",
        action="store_true",
        help="Ignore unknown characters instead of failing.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    value = gematria(args.text, language=args.language, strict=not args.lenient)
    print(value)


if __name__ == "__main__":
    main()
