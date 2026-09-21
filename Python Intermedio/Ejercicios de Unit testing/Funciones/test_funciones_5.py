import os
import unittest

from module_loader import load_module_from_file

MODULE_PATH = os.path.join(os.path.dirname(__file__), "funciones 5.py")
funciones_5 = load_module_from_file("funciones_5", MODULE_PATH)


class TestAuditTextCasing(unittest.TestCase):
    """Success-case tests for audit_text_casing (count upper/lower case letters)."""

    def test_counts_mixed_case_sentence(self):
        """Should correctly count uppercase and lowercase letters in a mixed sentence."""
        result = funciones_5.audit_text_casing("I love Python")

        self.assertEqual(
            result,
            "Analysis complete: 2 uppercase and 9 lowercase letters found.",
        )

    def test_counts_all_uppercase_string(self):
        """Should report zero lowercase letters for an all-uppercase string."""
        result = funciones_5.audit_text_casing("ALFA SEGURIDAD")

        self.assertEqual(
            result,
            "Analysis complete: 13 uppercase and 0 lowercase letters found.",
        )

    def test_ignores_digits_and_symbols(self):
        """Should ignore numbers and symbols, counting only letters."""
        result = funciones_5.audit_text_casing("Grupo Alfa 2026!!")

        self.assertEqual(
            result,
            "Analysis complete: 2 uppercase and 7 lowercase letters found.",
        )


if __name__ == "__main__":
    unittest.main()
