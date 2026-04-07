import unittest
from calculator import add, subtract, multiply, divide, power, is_even

class TestCalculator(unittest.TestCase):
    
    # Test 1: Addition
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        print("✅ Addition test passed")
    
    # Test 2: Subtraction
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
        print("✅ Subtraction test passed")
    
    # Test 3: Multiplication
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
        print("✅ Multiplication test passed")
    
    # Test 4: Division
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(-6, 2), -3)
        print("✅ Division test passed")
    
    # Test 5: Division by zero (expects error)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
        print("✅ Division by zero test passed")
    
    # Test 6: Power/Exponent
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, 2), 100)
        print("✅ Power test passed")
    
    # Test 7: Even number check
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(100))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(7))
        print("✅ Even number test passed")

if __name__ == "__main__":
    unittest.main()