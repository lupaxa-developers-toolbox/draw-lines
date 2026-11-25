"""draw_line layout, colour, and width."""

from __future__ import annotations

import os
import re
import shutil

import colorama
import pytest

from lupaxa.draw_lines import draw_line

_ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _visible(text: str) -> str:
    return _ANSI.sub("", text)


def test_zero_width_is_empty() -> None:
    assert draw_line(text="Hello", width=0) == ""


def test_empty_text_is_a_solid_rule() -> None:
    assert draw_line(width=90) == "-" * 90


def test_fill_char_uses_only_the_first_character() -> None:
    assert draw_line(width=4, fill_char="=*=") == "===="


def test_negative_width_uses_terminal_columns_minus_one(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(shutil, "get_terminal_size", lambda: os.terminal_size((40, 24)))
    assert draw_line(width=-1) == "-" * 39


def test_left_right_and_center() -> None:
    text = "Hello, World!"
    assert _visible(draw_line(text=text, position="left", width=90)).startswith("-- Hello, World! ")
    assert _visible(draw_line(text=text, position="right", width=90)).endswith(" Hello, World! --")
    centered = _visible(draw_line(text=text, position="center", width=90))
    assert centered.strip("-") == " Hello, World! "
    assert len(centered) == 90


def test_center_ignores_pad_and_keeps_one_space() -> None:
    line = _visible(draw_line(text="Hi", position="center", pad=0, fill_char=".", width=10))
    assert line == "... Hi ..."


def test_pad_zero_omits_the_gap() -> None:
    left = _visible(draw_line(text="Hi", position="left", pad=0, width=6))
    right = _visible(draw_line(text="Hi", position="right", pad=0, width=6))
    assert left == "Hi ---"
    assert right == "--- Hi"


def test_visible_length_matches_width() -> None:
    line = draw_line(text="Hello, World!", position="right", width=90, color="cyan+bold")
    assert len(_visible(line)) == 90
    assert "Hello, World!" in line


def test_color_codes_wrap_only_the_text() -> None:
    line = draw_line(text="Hi", position="right", width=10, color="cyan + bold#$%")
    assert colorama.Fore.CYAN in line
    assert colorama.Style.BRIGHT in line
    assert line.index(colorama.Fore.CYAN) < line.index("Hi") < line.index(colorama.Style.RESET_ALL)


def test_bold_alone() -> None:
    line = draw_line(text="Hi", position="left", width=10, color="bold")
    assert line.startswith(f"-- {colorama.Style.BRIGHT}Hi{colorama.Style.RESET_ALL} ")


def test_invalid_color_raises() -> None:
    with pytest.raises(ValueError, match="Invalid color component"):
        draw_line(text="Hi", width=10, color="purple")
    with pytest.raises(ValueError, match="Invalid color format"):
        draw_line(text="Hi", width=10, color="cyan+red")


def test_invalid_position_and_pad_raise() -> None:
    with pytest.raises(ValueError, match="position"):
        draw_line(text="Hi", position="middle", width=10)
    with pytest.raises(ValueError, match="pad"):
        draw_line(text="Hi", pad=-1, width=10)


def test_text_longer_than_width_is_returned_unchanged() -> None:
    line = draw_line(text="Hello, World!", position="center", width=4)
    assert _visible(line) == " Hello, World! "
