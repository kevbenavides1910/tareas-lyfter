"""
Big O Analysis: O(n * m)

For each element in list_a (size n), the entire list_b (size m) is
traversed. In the worst case (no match found), both lists are fully
traversed, giving n * m comparisons. If both lists are assumed to be
of similar size n, this is often expressed as O(n^2).
"""


def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
    return False


if __name__ == "__main__":
    print(check_if_lists_have_an_equal([1, 2, 3], [4, 5, 3]))
    print(check_if_lists_have_an_equal([1, 2, 3], [4, 5, 6]))
