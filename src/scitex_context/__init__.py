#!/usr/bin/env python3
"""scitex-context — execution-context detection (script vs notebook vs IPython) + output suppression."""

from __future__ import annotations

try:
    from importlib.metadata import version as _v, PackageNotFoundError
    try:
        __version__ = _v("scitex-context")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover — only on ancient Pythons
    __version__ = "0.0.0+local"
from ._detect_environment import (
    detect_environment,
    get_output_directory,
    is_ipython,
    is_notebook,
    is_script,
)
from ._embed import embed
from ._get_notebook_path import (
    get_notebook_directory,
    get_notebook_info_simple,
    get_notebook_name,
    get_notebook_path,
)
from ._less import less
from ._paste import paste
from ._suppress_output import quiet, suppress_output

__all__ = [
    "__version__",
    "detect_environment",
    "embed",
    "get_notebook_directory",
    "get_notebook_info_simple",
    "get_notebook_name",
    "get_notebook_path",
    "get_output_directory",
    "is_ipython",
    "is_notebook",
    "is_script",
    "less",
    "paste",
    "quiet",
    "suppress_output",
]
