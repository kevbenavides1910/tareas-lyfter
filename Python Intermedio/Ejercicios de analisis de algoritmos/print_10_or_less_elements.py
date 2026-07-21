"""
Big O Analysis: O(1)

The loop never runs more than 10 iterations, regardless of how large
list_to_print is. Its iteration count is bounded by a constant (10),
not by the input size n, so this runs in constant time.
"""


def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)
    for index in range(min(list_len, 10)):
        print(list_to_print[index])


if __name__ == "__main__":
    print_10_or_less_elements(list(range(25)))
