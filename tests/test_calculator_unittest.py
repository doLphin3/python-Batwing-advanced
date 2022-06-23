import unittest
from functions_to_test import Calculator


class TestCalculatorUnittest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(12, 1), 13)
        self.assertEqual(Calculator.add(0, 5), 5)
        self.assertEqual(Calculator.add(100, 44), 144)
        self.assertEqual(Calculator.add(45, 24), 69)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(14, 6), 8)
        self.assertEqual(Calculator.subtract(1, 5), -4)
        self.assertEqual(Calculator.subtract(14, -1), 15)
        self.assertEqual(Calculator.subtract(-6, 6), -12)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4, 3), 12)
        self.assertEqual(Calculator.multiply(6, 3), 18)
        self.assertEqual(Calculator.multiply(9, 0), 0)
        self.assertEqual(Calculator.multiply(-2, 4), -8)

    def test_divide(self):
        self.assertRaises(ValueError, Calculator.divide, 5, 0)
        self.assertEqual(Calculator.divide(8, 2), 4)
        self.assertEqual(Calculator.divide(45, 9), 5)
        self.assertEqual(Calculator.divide(18, -6), -3)
        self.assertEqual(Calculator.divide(8, -8), -1)
