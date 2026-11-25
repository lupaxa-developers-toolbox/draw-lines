"""lupaxa.draw_lines — coloured rules for the terminal.

``draw_line()`` returns one line. Place optional text on the left, in the
centre, or on the right, and colour it with a name such as ``cyan`` or
``cyan+bold``.
"""

from __future__ import annotations

from .lines import draw_line
from .version import __version__, get_version

__all__ = [
    "__version__",
    "draw_line",
    "get_version",
]
