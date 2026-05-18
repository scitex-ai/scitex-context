#!/usr/bin/env python3
# Timestamp: "2025-06-02 16:30:00 (claude)"
# File: ./tests/scitex/context/test__suppress_output.py
# ----------------------------------------

"""
Comprehensive test suite for scitex.context._suppress_output module.

This module tests the suppress_output context manager for stdout/stderr suppression.

Test Structure:
- Basic output suppression functionality
- Conditional suppression behavior
- Error handling and edge cases
- Integration with different output types
- Alias testing (quiet)
"""

import sys
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

import pytest

from scitex_context._suppress_output import quiet, suppress_output


class TestSuppressOutput:
    """Test cases for the suppress_output context manager."""

    def test_suppress_output_is_callable_after_import(self):
        # Arrange
        target = suppress_output

        # Act
        is_callable = callable(target)

        # Assert
        assert is_callable, "suppress_output should be callable"

    def test_suppress_output_hides_stdout_inside_block(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output():
                print("This should be suppressed")
        observed = captured_output.getvalue()

        # Assert
        assert "This should be suppressed" not in observed

    def test_suppress_output_restores_stdout_after_block(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output():
                print("This should be suppressed")
            print("This should be visible")
        observed = captured_output.getvalue()

        # Assert
        assert "This should be visible" in observed

    def test_suppress_output_hides_stderr_inside_block(self):
        # Arrange
        captured_error = StringIO()

        # Act
        with redirect_stderr(captured_error):
            with suppress_output():
                print("This should be suppressed to stderr", file=sys.stderr)
        observed = captured_error.getvalue()

        # Assert
        assert "This should be suppressed to stderr" not in observed

    def test_suppress_output_restores_stderr_after_block(self):
        # Arrange
        captured_error = StringIO()

        # Act
        with redirect_stderr(captured_error):
            with suppress_output():
                print("Suppressed", file=sys.stderr)
            print("This should be visible to stderr", file=sys.stderr)
        observed = captured_error.getvalue()

        # Assert
        assert "This should be visible to stderr" in observed

    def test_suppress_output_hides_stdout_when_both_streams_active(self):
        # Arrange
        captured_output = StringIO()
        captured_error = StringIO()

        # Act
        with redirect_stdout(captured_output), redirect_stderr(captured_error):
            with suppress_output():
                print("Suppressed stdout")
                print("Suppressed stderr", file=sys.stderr)
        observed = captured_output.getvalue()

        # Assert
        assert "Suppressed stdout" not in observed

    def test_suppress_output_hides_stderr_when_both_streams_active(self):
        # Arrange
        captured_output = StringIO()
        captured_error = StringIO()

        # Act
        with redirect_stdout(captured_output), redirect_stderr(captured_error):
            with suppress_output():
                print("Suppressed stdout")
                print("Suppressed stderr", file=sys.stderr)
        observed = captured_error.getvalue()

        # Assert
        assert "Suppressed stderr" not in observed

    def test_suppress_output_with_suppress_false_passes_stdout_through(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output(suppress=False):
                print("This should be visible")
        observed = captured_output.getvalue()

        # Assert
        assert "This should be visible" in observed

    def test_suppress_output_with_explicit_suppress_true_hides_stdout(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output(suppress=True):
                print("This should be suppressed")
        observed = captured_output.getvalue()

        # Assert
        assert "This should be suppressed" not in observed

    def test_nested_suppress_output_blocks_hide_inner_print(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output():
                with suppress_output():
                    print("Inner suppressed")
        observed = captured_output.getvalue()

        # Assert
        assert "Inner suppressed" not in observed

    def test_nested_suppress_output_blocks_restore_outer_print(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output():
                pass
            print("After outer context")
        observed = captured_output.getvalue()

        # Assert
        assert "After outer context" in observed

    def test_mixed_nested_contexts_pass_outer_when_false(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output(suppress=False):
                print("Outer not suppressed")
                with suppress_output(suppress=True):
                    pass
        observed = captured_output.getvalue()

        # Assert
        assert "Outer not suppressed" in observed

    def test_mixed_nested_contexts_hide_inner_when_true(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output(suppress=False):
                with suppress_output(suppress=True):
                    print("Inner suppressed")
        observed = captured_output.getvalue()

        # Assert
        assert "Inner suppressed" not in observed

    def test_suppress_output_propagates_value_error_from_block(self):
        # Arrange
        def raises_value_error():
            with suppress_output():
                raise ValueError("Test exception")

        # Act
        action = raises_value_error

        # Assert
        with pytest.raises(ValueError):
            action()

    def test_suppress_output_returns_value_from_called_function(self):
        # Arrange
        def inner():
            print("This should be suppressed")
            return "test_value"

        # Act
        with suppress_output():
            result = inner()

        # Assert
        assert result == "test_value"

    def test_quiet_alias_is_same_object_as_suppress_output(self):
        # Arrange
        a = quiet
        b = suppress_output

        # Act
        same = a is b

        # Assert
        assert same

    def test_quiet_alias_hides_stdout_inside_block(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with quiet():
                print("This should be suppressed by quiet")
        observed = captured_output.getvalue()

        # Assert
        assert "This should be suppressed by quiet" not in observed

    def test_suppress_output_instance_implements_enter_method(self):
        # Arrange
        context_manager = suppress_output()

        # Act
        has_enter = hasattr(context_manager, "__enter__")

        # Assert
        assert has_enter

    def test_suppress_output_instance_implements_exit_method(self):
        # Arrange
        context_manager = suppress_output()

        # Act
        has_exit = hasattr(context_manager, "__exit__")

        # Assert
        assert has_exit

    def test_suppress_output_manual_enter_exit_hides_stdout(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            cm = suppress_output()
            cm.__enter__()
            try:
                print("Manually suppressed")
            finally:
                cm.__exit__(None, None, None)
        observed = captured_output.getvalue()

        # Assert
        assert "Manually suppressed" not in observed

    def test_suppress_output_handles_large_volume_of_output_lines(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output():
                for i in range(1000):
                    print(f"Line {i} should be suppressed")
        observed = captured_output.getvalue()

        # Assert
        assert "Line 999 should be suppressed" not in observed

    def test_suppress_output_hides_sys_stdout_write_calls(self):
        # Arrange
        captured_output = StringIO()

        # Act
        with redirect_stdout(captured_output):
            with suppress_output():
                sys.stdout.write("Direct stdout write\n")
        observed = captured_output.getvalue()

        # Assert
        assert len(observed) == 0

    def test_suppress_output_hides_sys_stderr_write_calls(self):
        # Arrange
        captured_error = StringIO()

        # Act
        with redirect_stderr(captured_error):
            with suppress_output():
                sys.stderr.write("Direct stderr write\n")
        observed = captured_error.getvalue()

        # Assert
        assert len(observed) == 0


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])

# EOF
