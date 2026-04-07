"""Unit tests for addition operation only."""
import unittest
from calculator import add

class TestAddition(unittest.TestCase):
    """Test cases for addition operation."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)
        print("✅ Addition positive: 2 + 3 = 5")
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add(-1, -1), -2)
        print("✅ Addition negative: -1 + -1 = -2")
    
    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        self.assertEqual(add(-1, 1), 0)
        print("✅ Addition mixed: -1 + 1 = 0")
    
    def test_add_with_zero(self):
        """Test adding zero."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)
        print("✅ Addition with zero: 0 + 5 = 5")

if __name__ == "__main__":
    unittest.main()