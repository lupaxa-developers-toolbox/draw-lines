"""Draw a coloured rule across the terminal, with optional text."""

from __future__ import annotations

import re
import shutil

import colorama

colorama.just_fix_windows_console()

_COLORS: dict[str, str] = {
    "black": colorama.Fore.BLACK,
    "blue": colorama.Fore.BLUE,
    "cyan": colorama.Fore.CYAN,
    "green": colorama.Fore.GREEN,
    "grey": colorama.Fore.LIGHTBLACK_EX,
    "magenta": colorama.Fore.MAGENTA,
    "red": colorama.Fore.RED,
    "white": colorama.Fore.WHITE,
    "yellow": colorama.Fore.YELLOW,
    "bold": colorama.Style.BRIGHT,
    "reset": colorama.Style.RESET_ALL,
}

_POSITIONS = frozenset({"left", "center", "right"})
_COLOR_CLEAN = re.compile(r"[^a-zA-Z+]")


def _first_character(text: str) -> str:
    """Return the first character of ``text``, or an empty string."""
    if text:
        return text[0]
    return ""


def _color_codes(color: str) -> tuple[str, str]:
    """Return ``(colour_code, reset_code)`` for a colour expression.

    Accepted forms are ``colour``, ``colour+bold``, ``bold+colour``, and
    ``bold``. Anything other than letters and ``+`` is ignored.
    """
    if not color:
        return "", ""

    sanitized = _COLOR_CLEAN.sub("", color).lower()
    parts = sanitized.split("+")
    if len(parts) > 2 or (len(parts) == 2 and "bold" not in parts):
        raise ValueError("Invalid color format. Use 'color', 'color+bold', or 'bold'.")

    color_code = ""
    for part in parts:
        if part not in _COLORS:
            allowed = ", ".join(_COLORS)
            raise ValueError(f"Invalid color component '{part}'. Allowed values are: {allowed}")
        color_code += _COLORS[part]

    reset_code = _COLORS["reset"] if color_code else ""
    return color_code, reset_code


def _display_text(text: str, position: str, fill_char: str, pad: int, color_code: str, reset_code: str) -> str:
    """Build the text segment, including padding and colour codes."""
    if position == "left":
        gap = " " if pad > 0 else ""
        return f"{fill_char * pad}{gap}{color_code}{text}{reset_code} "
    if position == "right":
        gap = " " if pad > 0 else ""
        return f" {color_code}{text}{reset_code}{gap}{fill_char * pad}"
    return f" {color_code}{text}{reset_code} "


def draw_line(text: str = "", position: str = "center", fill_char: str = "-", pad: int = 2, width: int = -1, color: str = "") -> str:
    """Draw a line with optional text on the left, centre, or right.

    Args:
        text: Text to place on the line. An empty string draws a solid rule.
        position: ``left``, ``center``, or ``right``.
        fill_char: Character used for the rule and for side padding. Only the
            first character is used.
        pad: Fill characters beside the text. Used for ``left`` and ``right``.
            ``center`` always keeps a single space on each side of the text.
        width: Line width. ``-1`` uses the terminal width minus one column.
            ``0`` returns an empty string.
        color: Colour name, ``bold``, or ``colour+bold`` (for example
            ``cyan+bold``). Punctuation and spaces are ignored.

    Returns:
        The constructed line, including ANSI colour codes when ``color`` is set.
    """
    if width == 0:
        return ""
    if pad < 0:
        raise ValueError("pad must be zero or greater")
    if position not in _POSITIONS:
        raise ValueError("position must be 'left', 'center', or 'right'")

    terminal_width = shutil.get_terminal_size().columns - 1 if width < 0 else width

    fill = _first_character(fill_char)
    if not text:
        return fill * terminal_width

    color_code, reset_code = _color_codes(color)
    segment = _display_text(text, position, fill, pad, color_code, reset_code)
    text_len = len(segment) - len(color_code) - len(reset_code)
    if text_len >= terminal_width:
        return segment

    remaining = terminal_width - text_len
    if position == "left":
        return f"{segment}{fill * remaining}"
    if position == "right":
        return f"{fill * remaining}{segment}"

    left_padding = remaining // 2
    right_padding = remaining - left_padding
    return f"{fill * left_padding}{segment}{fill * right_padding}"
