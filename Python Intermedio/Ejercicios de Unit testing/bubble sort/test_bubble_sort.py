import random
import unittest

from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Unit tests for the bubble_sort function."""

    def test_sorts_small_list(self):
        """bubble_sort should correctly sort a small list of integers."""
        input_list = [5, 3, 8, 1, 2]
        expected = [1, 2, 3, 5, 8]

        result = bubble_sort(input_list)

        self.assertEqual(result, expected)

    def test_sorts_large_list(self):
        """bubble_sort should correctly sort a list with more than 100 elements."""
        random.seed(42)
        input_list = [random.randint(-1000, 1000) for _ in range(150)]
        expected = sorted(input_list)

        result = bubble_sort(input_list)

        self.assertEqual(result, expected)
        self.assertEqual(len(result), 150)

    def test_sorts_empty_list(self):
        """bubble_sort should return an empty list when given an empty list."""
        input_list = []

        result = bubble_sort(input_list)

        self.assertEqual(result, [])

    def test_raises_error_for_non_list_parameter(self):
        """bubble_sort should raise a TypeError when the argument is not a list."""
        invalid_inputs = ["not a list", 42, 3.14, {"a": 1}, ("tuple", "of", "values"), None]

        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError):
                    bubble_sort(invalid_input)


if __name__ == "__main__":
    unittest.main()
