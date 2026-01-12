"""Core gematria calculation helpers."""

from __future__ import annotations

import string
from typing import Mapping

from gematria_tool.mappings import LANGUAGE_MAPS


PUNCTUATION = set(string.whitespace + string.punctuation)


def normalize(text: str) -> str:
    """Normalize input text by stripping punctuation and whitespace."""
    return "".join(ch for ch in text if ch not in PUNCTUATION)


def gematria(
    text: str,
    *,
    language: str = "hebrew",
    mapping: Mapping[str, int] | None = None,
    strict: bool = True,
) -> int:
    """Compute the gematria/isopsephy value for ``text``.

    Args:
        text: Input string to evaluate.
        language: One of "hebrew" or "greek".
        mapping: Optional custom mapping to override the language default.
        strict: When True, unknown characters raise a ValueError.
            When False, unknown characters are ignored.

    Returns:
        Integer sum for all recognized letters.
    """
    if mapping is None:
        if language not in LANGUAGE_MAPS:
            raise ValueError(
                f"Unsupported language '{language}'."
                " Use 'hebrew' or 'greek', or supply a custom mapping."
            )
        mapping = LANGUAGE_MAPS[language]

    total = 0
    normalized = normalize(text)
    for char in normalized:
        value = mapping.get(char)
        if value is None:
            if strict:
                raise ValueError(
                    f"Character '{char}' not found in mapping for '{language}'."
                )
            continue
        total += value
    return total
