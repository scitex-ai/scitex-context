#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: /tests/scitex_context/test__paste.py
"""Smoke tests for ``scitex_context.paste`` (ported from scitex_gen._ipython._paste).

The function relies on the optional ``pyperclip`` dep; the module itself
imports it inside the function body so ``import scitex_context.paste``
succeeds even when pyperclip is missing. Tests below confirm:

1. The symbol is importable from both the package and the submodule.
2. When pyperclip is unavailable, calling ``paste()`` swallows the
   ``ImportError`` (caught by the broad except) and prints a message.
"""

from __future__ import annotations

import sys

import pytest

from scitex_context import paste
from scitex_context._paste import paste as paste_direct


def test_paste_is_importable():
    assert callable(paste)
    assert callable(paste_direct)
    assert paste is paste_direct


def test_paste_no_pyperclip_does_not_raise(monkeypatch, capsys):
    """If pyperclip is absent, ``paste()`` catches the ImportError and
    prints, instead of propagating."""
    # Force the pyperclip import inside paste() to fail.
    monkeypatch.setitem(sys.modules, "pyperclip", None)
    paste()
    captured = capsys.readouterr()
    assert "Could not execute clipboard content" in captured.out


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])
