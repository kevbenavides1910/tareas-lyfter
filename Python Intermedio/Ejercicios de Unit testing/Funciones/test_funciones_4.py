import os
import unittest

from module_loader import load_module_from_file

MODULE_PATH = os.path.join(os.path.dirname(__file__), "Funciones 4.py")
funciones_4 = load_module_from_file("funciones_4", MODULE_PATH)


class TestEncryptCorporateData(unittest.TestCase):
    """Success-case tests for encrypt_corporate_data (reverse a string)."""

    def test_reverses_a_phrase_with_spaces(self):
        """Should reverse a full phrase, including spaces, character by character."""
        result = funciones_4.encrypt_corporate_data("Hola mundo")

        self.assertEqual(result, "odnum aloH")

    def test_reverses_a_single_word(self):
        """Should reverse a single word correctly."""
        result = funciones_4.encrypt_corporate_data("Python")

        self.assertEqual(result, "nohtyP")

    def test_reverses_a_string_with_numbers_and_symbols(self):
        """Should reverse a string that mixes letters, numbers, and symbols."""
        result = funciones_4.encrypt_corporate_data("Alfa-2026!")

        self.assertEqual(result, "!6202-aflA")


if __name__ == "__main__":
    unittest.main()
