import os
import unittest

from module_loader import load_module_from_file

MODULE_PATH = os.path.join(os.path.dirname(__file__), "funciones 7.py")
funciones_7 = load_module_from_file("funciones_7", MODULE_PATH, mock_input_value="1")


class TestCheckPrimeSecurity(unittest.TestCase):
    """Success-case tests for check_prime_security (single-number prime check)."""

    def test_identifies_a_prime_number(self):
        """Should return True for a known prime number."""
        self.assertTrue(funciones_7.check_prime_security(13))

    def test_identifies_a_non_prime_number(self):
        """Should return False for a known composite number."""
        self.assertFalse(funciones_7.check_prime_security(9))

    def test_identifies_numbers_below_two_as_not_prime(self):
        """Should return False for numbers less than 2 (0, 1, negatives)."""
        self.assertFalse(funciones_7.check_prime_security(1))
        self.assertFalse(funciones_7.check_prime_security(0))
        self.assertFalse(funciones_7.check_prime_security(-5))


class TestExtractValidTokens(unittest.TestCase):
    """Success-case tests for extract_valid_tokens (filter primes from a comma-separated string)."""

    def test_filters_primes_from_example_input(self):
        """Should reproduce the exact example from the exercise statement."""
        result = funciones_7.extract_valid_tokens("1,4,6,7,13,9,67")

        self.assertEqual(result, [7, 13, 67])

    def test_returns_empty_list_when_no_primes_present(self):
        """Should return an empty list when none of the numbers are prime."""
        result = funciones_7.extract_valid_tokens("1,4,6,8,9")

        self.assertEqual(result, [])

    def test_handles_spaces_around_numbers(self):
        """Should correctly parse numbers even with extra spaces around commas."""
        result = funciones_7.extract_valid_tokens("2, 10, 11, 15, 17")

        self.assertEqual(result, [2, 11, 17])


if __name__ == "__main__":
    unittest.main()
