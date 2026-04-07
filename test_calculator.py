"""Unit tests for calculator module."""
import unittest
from calculator import add, subtract, multiply, divide, power, is_even

class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations."""
    
    def test_add(self):
        """Test addition operation."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division operation."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(-6, 2), -3)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_power(self):
        """Test exponentiation operation."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, 2), 100)
    
    def test_is_even(self):
        """Test even number detection."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(100))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(7))

if __name__ == "__main__":
    unittest.main()