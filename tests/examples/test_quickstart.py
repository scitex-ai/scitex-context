"""Compile-only stub for examples/quickstart.py (PS303)."""

import subprocess
import sys
from pathlib import Path

QUICKSTART = Path(__file__).parents[2] / "examples" / "quickstart.py"


def test_quickstart_file_exists_at_examples_dir():
    # Arrange
    target = QUICKSTART

    # Act
    is_file = target.is_file()

    # Assert
    assert is_file, f"missing {target}"


def test_quickstart_compiles_without_syntax_error():
    # Arrange
    target = QUICKSTART

    # Act
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(target)],
        check=False,
    )

    # Assert
    assert result.returncode == 0
