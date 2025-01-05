import unittest
from math_utils import multiply

class TestMathUtils (unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 2), 6)
    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, -4), 8)
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 10), 0)


if __name__ == '__main__':
    unittest.main()
