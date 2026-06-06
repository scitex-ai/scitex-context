#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2024-11-03 02:13:54 (ywatanabe)"
# File: ./src/scitex_context/_paste.py
"""Execute the current clipboard content as Python source.

Ported from scitex_gen._ipython._paste (Phase B retirement wave).
Requires the optional ``pyperclip`` dep.
"""

from __future__ import annotations


def paste():
    """Read the current clipboard text and ``exec`` it as Python source.

    Errors during execution are caught and printed; no exception escapes.
    """
    import textwrap

    import pyperclip

    try:
        clipboard_content = pyperclip.paste()
        clipboard_content = textwrap.dedent(clipboard_content)
        exec(clipboard_content)
    except Exception as e:
        print(f"Could not execute clipboard content: {e}")


# EOF
