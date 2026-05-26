"""Tests for calculator functions."""

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_multiply_positive_integers(self):
        """Test multiply function with positive integers."""
        result = multiply(3, 4)
        self.assertEqual(result, 12)
        
    def test_multiply_with_zero(self):
        """Test multiply function with zero."""
        result = multiply(0, 5)
        self.assertEqual(result, 0)
        
    def test_multiply_negative_numbers(self):
        """Test multiply function with negative numbers."""
        result = multiply(-2, 3)
        self.assertEqual(result, -6)
        
    def test_multiply_floats(self):
        """Test multiply function with float numbers."""
        result = multiply(2.5, 4)
        self.assertEqual(result, 10.0)
        
    def test_multiply_returns_value(self):
        """Test that multiply function actually returns a value (not None)."""
        result = multiply(1, 1)
        self.assertIsNotNone(result, "multiply function should return a value, not None")
        
    # Test other functions to ensure they still work
    def test_add_function(self):
        """Test add function still works."""
        result = add(2, 3)
        self.assertEqual(result, 5)
        
    def test_subtract_function(self):
        """Test subtract function still works."""
        result = subtract(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
