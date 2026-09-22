"""Smoke: installed package imports and detects the script context (PS-211).

Subprocess-driven (``sys.executable <tmp script>``) so this proves the
installed distribution resolves — an in-process import would not. A real
``.py`` file is required: the detector reports ``script`` only when
``sys.argv[0]`` ends in ``.py`` (``python -c`` reads ``unknown``).
Hermetic: no network, no credentials, no writes outside tmp dirs.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.smoke

_PROBE = (
    "import scitex_context as ctx\n"
    "print(ctx.detect_environment())\n"
    "print(ctx.is_script())\n"
    "print(ctx.is_notebook())\n"
)


def test_subprocess_import_reports_script_execution_context(tmp_path: Path) -> None:
    # Arrange
    probe = tmp_path / "probe_context.py"
    probe.write_text(_PROBE)
    argv = [sys.executable, str(probe)]

    # Act
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=30)

    # Assert
    assert (completed.returncode, completed.stdout.split()) == (0, ["script", "True", "False"])
