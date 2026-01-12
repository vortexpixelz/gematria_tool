import pytest

from gematria_tool import gematria
from gematria_tool.core import normalize


def test_normalize_strips_punctuation():
    assert normalize("λόγος!") == "λόγος"


def test_gematria_hebrew():
    assert gematria("בראשית", language="hebrew") == 913


def test_gematria_greek():
    assert gematria("λογος", language="greek") == 373


def test_gematria_lenient():
    assert gematria("λογος?", language="greek", strict=False) == 373


def test_gematria_unknown_character_raises():
    with pytest.raises(ValueError):
        gematria("λογοςx", language="greek", strict=True)
