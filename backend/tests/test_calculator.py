import unittest
from backend.calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self):
        operand1 = 5
        operand2 = 10

        expected_sum = 15
        actual_sum = sum(operand1, operand2)
        self.assertEqual(expected_sum, actual_sum, "Expected and actual sum differ")

    def test_subtract(self):
        operand1 = 4
        operand2 = 10

        expected_difference = -6
        actual_difference = subtract(operand1, operand2)
        self.assertEqual(expected_difference, actual_difference, "Expected and actual difference differ")

if __name__ == '__main__':
    unittest.main()
