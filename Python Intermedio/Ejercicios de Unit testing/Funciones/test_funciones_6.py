import os
import unittest

from module_loader import load_module_from_file

MODULE_PATH = os.path.join(os.path.dirname(__file__), "funciones 6.py")
funciones_6 = load_module_from_file("funciones_6", MODULE_PATH)


class TestOrganizeInventoryReport(unittest.TestCase):
    """Success-case tests for organize_inventory_report (alphabetically sort hyphen-separated words)."""

    def test_sorts_words_from_the_example(self):
        """Should reproduce the exact example from the exercise statement."""
        result = funciones_6.organize_inventory_report(
            "python-variable-funcion-computadora-monitor"
        )

        self.assertEqual(
            result, "computadora-funcion-monitor-python-variable"
        )

    def test_sorts_two_words(self):
        """Should correctly sort a simple two-word input."""
        result = funciones_6.organize_inventory_report("mouse-teclado")

        self.assertEqual(result, "mouse-teclado")

    def test_sorts_already_sorted_input(self):
        """Should return the same string when the input is already sorted."""
        result = funciones_6.organize_inventory_report("cable-disco-router")

        self.assertEqual(result, "cable-disco-router")


if __name__ == "__main__":
    unittest.main()
