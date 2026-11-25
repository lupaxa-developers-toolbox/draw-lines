"""Package layout."""

from __future__ import annotations

import importlib.machinery
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = REPO_ROOT / "src" / "lupaxa" / "draw_lines"
SRC = REPO_ROOT / "src"


def test_namespace_package_has_no_init() -> None:
    assert not (SRC / "lupaxa" / "__init__.py").is_file()


def test_lupaxa_portion_is_a_namespace() -> None:
    spec = importlib.machinery.PathFinder.find_spec("lupaxa", [str(SRC)])
    assert spec is not None
    assert spec.loader is None


def test_package_modules_exist() -> None:
    assert (PKG / "__init__.py").is_file()
    assert (PKG / "lines.py").is_file()
    assert (PKG / "version.py").is_file()
    assert (PKG / "py.typed").is_file()


def test_root_script_is_not_the_library() -> None:
    assert not (REPO_ROOT / "draw_lines.py").is_file()
    assert not (REPO_ROOT / "setup.cfg").is_file()
    assert not (REPO_ROOT / "mkdocs.yml").is_file()
