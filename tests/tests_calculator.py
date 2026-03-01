import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from calculator import calculate


class TestCalculatorExpressions(unittest.TestCase):
    def test_minus_minus(self):
        self.assertEqual(calculate("8--8"), 16)

    def test_unary_minus_with_addition(self):
        self.assertEqual(calculate("-2+3"), 1)

    def test_power_operator(self):
        self.assertEqual(calculate("2**2"), 4)

    def test_unary_minus_with_multiplication(self):
        self.assertEqual(calculate("2*-3"), -6)

    def test_reject_multiple_binary_operators(self):
        with self.assertRaises(ValueError):
            calculate("2+3*4")


if __name__ == "__main__":
    unittest.main()
