"""Test cases for subtract_all function to verify issue #6 fix."""

from calculator import subtract_all


def test_subtract_all_empty_input():
    """Test that subtract_all() returns 0 for empty input (fixes issue #6)."""
    result = subtract_all()
    assert result == 0, f"Expected 0, but got {result}"
    print("✓ subtract_all() correctly returns 0 for empty input")


def test_subtract_all_single_argument():
    """Test that subtract_all(x) returns x."""
    result = subtract_all(42)
    assert result == 42, f"Expected 42, but got {result}"
    print("✓ subtract_all(42) correctly returns 42")


def test_subtract_all_multiple_arguments():
    """Test that subtract_all works correctly with multiple arguments."""
    # Test: 10 - 3 - 2 = 5
    result = subtract_all(10, 3, 2)
    assert result == 5, f"Expected 5, but got {result}"
    print("✓ subtract_all(10, 3, 2) correctly returns 5")
    
    # Test: 100 - 10 - 20 - 30 = 40
    result = subtract_all(100, 10, 20, 30)
    assert result == 40, f"Expected 40, but got {result}"
    print("✓ subtract_all(100, 10, 20, 30) correctly returns 40")


def test_subtract_all_negative_numbers():
    """Test that subtract_all works with negative numbers."""
    # Test: 10 - (-5) = 15
    result = subtract_all(10, -5)
    assert result == 15, f"Expected 15, but got {result}"
    print("✓ subtract_all(10, -5) correctly returns 15")


if __name__ == "__main__":
    print("Running tests for subtract_all function...")
    test_subtract_all_empty_input()
    test_subtract_all_single_argument() 
    test_subtract_all_multiple_arguments()
    test_subtract_all_negative_numbers()
    print("\n🎉 All tests passed! Issue #6 has been fixed.")
