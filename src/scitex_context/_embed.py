#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: ./src/scitex_context/_embed.py
"""Start an IPython embed session, optionally executing clipboard content first.

Ported from scitex_gen._ipython._embed (Phase B retirement wave).
Requires the optional ``IPython`` + ``pyperclip`` deps.
"""

from __future__ import annotations


def embed():
    """Start an IPython embed session and optionally execute clipboard content.

    Prompts the user whether to execute the current clipboard text.
    If confirmed, the contents are run in the embedded shell.

    Requires the optional dependencies ``IPython`` and ``pyperclip``.
    A clean ``ImportError`` is raised if either is missing.
    """
    import pyperclip
    from IPython import embed as _embed

    try:
        clipboard_content = pyperclip.paste()
    except pyperclip.PyperclipException as e:
        clipboard_content = ""
        print("Could not access the clipboard:", e)

    print("Clipboard content loaded. Do you want to execute it? [y/n]")
    execute_clipboard = input().strip().lower() == "y"

    # Start IPython shell
    ipython_shell = _embed(
        header=(
            "IPython is now running. Clipboard content will be executed"
            " if confirmed."
        )
    )

    # Execute if confirmed
    if clipboard_content and execute_clipboard:
        ipython_shell.run_cell(clipboard_content)


# EOF
