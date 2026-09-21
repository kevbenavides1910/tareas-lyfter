"""
Big O Analysis: O(n)

A single loop iterates over the list once, and each operation inside
(multiplication and print) is O(1). Total time grows linearly with
the size of numbers_list.
"""


def print_numbers_times_2(numbers_list):
    for number in numbers_list:
        print(number * 2)


if __name__ == "__main__":
    print_numbers_times_2([1, 2, 3, 4, 5])
