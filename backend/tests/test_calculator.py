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

    def test_multiplication(self):
        operand1 = 5
        operand2 = -3

        expected_multiplier = -15
        actual_multiplier = multiplication(operand1, operand2)
        self.assertEqual(expected_multiplier, actual_multiplier, "Expected and actual multiplier differ")

    def test_division_zero(self):
        operand1 = 3
        operand2 = 0

        expected_expection = Exception("division by zero not allowed")
        try:
            division(operand1, operand2)
        except Exception as actual_exception:
            self.assertEqual(str(expected_expection), str(actual_exception), "Division by zero not valid")

    def test_division(self):
        operand1 = 10
        operand2 = 2

        expected_dividend = 5.0
        actual_dividend = division(operand1, operand2)
        self.assertEqual(expected_dividend, actual_dividend, "Expected and actual dividend differ")

    def test_incorrect_operator(self):
        operator1 = 4
        operator2 = 2
        operation = '@'

        expected_exception = Exception("Operator not supported")

        try:
            perform_operation(operator1, operator2, operation)
        except Exception as actual_exception:
            self.assertEqual(str(expected_exception), str(actual_exception), "Operator provided not valid")

    def test_is_operation_supported(self):
        operation = '+'

        actual_operation = is_operator_supported(operation)
        expected_operation = True
        self.assertEqual(expected_operation, actual_operation, "this operation is not in the list")

    def test_perform_operation(self):
        operand1 = 5
        operand2 = 10
        operator = '+'

        actual_result = perform_operation(operand1, operand2, operator)
        expected_result = 15

        self.assertEqual(expected_result, actual_result, "Expected and actual results differ")


if __name__ == '__main__':
    unittest.main()
