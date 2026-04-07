import unittest
from calculator import multiply

class TestMultiplication(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(4, 5), 20)
    
    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)
    
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 100), 0)

if __name__ == "__main__":
    unittest.main()