import os
import unittest

from module_loader import load_module_from_file

MODULE_PATH = os.path.join(os.path.dirname(__file__), "funciones 3.py")
funciones_3 = load_module_from_file("funciones_3", MODULE_PATH)


class TestCalculateTotalPayout(unittest.TestCase):
    """Success-case tests for calculate_total_payout (sum of all numbers in a list)."""

    def test_sums_positive_numbers(self):
        """Should return the correct sum for a list of positive integers."""
        result = funciones_3.calculate_total_payout([4, 6, 2, 29])

        self.assertEqual(result, 41)

    def test_sums_list_with_negative_and_zero_values(self):
        """Should correctly handle a mix of negative numbers and zero."""
        result = funciones_3.calculate_total_payout([10, -3, 0, -2, 5])

        self.assertEqual(result, 10)

    def test_sums_list_with_decimal_values(self):
        """Should correctly sum a list containing float values."""
        result = funciones_3.calculate_total_payout([1.5, 2.5, 3])

        self.assertEqual(result, 7.0)


if __name__ == "__main__":
    unittest.main()
