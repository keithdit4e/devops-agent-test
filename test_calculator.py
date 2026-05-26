"""Tests for calculator functions."""

import pytest
from calculator import add, subtract, multiply, divide, greet
from io import StringIO
import sys


def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(-1, 1) == -2


def test_multiply():
    """Test multiplication function - this addresses issue #5."""
    # These tests would fail before the fix due to missing return statement
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 4) == 10.0
    assert multiply(-1, -1) == 1
    
    # Verify the function returns a value, not None
    result = multiply(2, 3)
    assert result is not None
    assert isinstance(result, (int, float))


def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(-6, 3) == -2


def test_greet():
    """Test greet function (note: this currently prints instead of returning)."""
    # Capture stdout to test the print behavior
    old_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    result = greet("Alice")
    
    sys.stdout = old_stdout
    output = captured_output.getvalue()
    
    assert "Hello, Alice!" in output
    # Note: this function currently prints instead of returning (another bug)
    assert result is None


if __name__ == "__main__":
    # Run tests manually if pytest is not available
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_greet()
    print("All tests passed!")
