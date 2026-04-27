"""Quickstart for scitex_context.

Detects the runtime environment and demonstrates the `quiet` /
`suppress_output` context managers.
"""

import io
import sys

import scitex_context as sc


def main() -> int:
    # Where are we running?
    env = sc.detect_environment()
    print(f"Runtime environment: {env}")
    print(f"is_script:   {sc.is_script()}")
    print(f"is_notebook: {sc.is_notebook()}")
    print(f"is_ipython:  {sc.is_ipython()}")

    # suppress_output: hide noisy prints from a third-party call
    with sc.suppress_output():
        print("THIS LINE IS HIDDEN", file=sys.stdout)
        print("AND THIS ONE TOO", file=sys.stderr)
    print("(visible again)")

    # quiet() is the documented alias
    captured = io.StringIO()
    sys.stdout = captured
    try:
        with sc.quiet():
            print("hidden inside quiet()")
        print("visible after quiet()")
    finally:
        sys.stdout = sys.__stdout__
    out = captured.getvalue()
    assert "hidden" not in out
    assert "visible after quiet()" in out
    print("quiet() correctly suppressed output inside the block.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
