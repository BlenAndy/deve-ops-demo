import unittest
from calculator import subtract

class TestSubtraction(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 5), 5)
    
    def test_subtract_negative(self):
        self.assertEqual(subtract(-1, -1), 0)
    
    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 5), -5)

if __name__ == "__main__":
    unittest.main()