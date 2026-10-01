"""E2E: detect the script context, then suppress a noisy call (PS-212).

The full story — a real ``.py`` probe run as a subprocess reports
``script`` via ``detect_environment()``, and a noisy function run under
``suppress_output()`` leaves no trace in its stdout. Real code paths,
real filesystem, no network. Gated on ``RUN_E2E=1`` (skipped by default).
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = [
    pytest.mark.e2e,
    pytest.mark.skipif(
        os.environ.get("RUN_E2E") != "1",
        reason="e2e: set RUN_E2E=1 to run end-to-end workflows",
    ),
]

_PROBE = (
    "import scitex_context as ctx\n"
    "print(ctx.detect_environment())\n"
    "def _noisy():\n"
    "    print('noise')\n"
    "with ctx.suppress_output():\n"
    "    _noisy()\n"
    "print('done')\n"
)


def test_detect_script_context_then_suppress_noisy_output(tmp_path: Path) -> None:
    # Arrange
    probe = tmp_path / "probe_e2e.py"
    probe.write_text(_PROBE)
    argv = [sys.executable, str(probe)]

    # Act
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=60)

    # Assert
    assert (completed.returncode, completed.stdout.split()) == (0, ["script", "done"])
