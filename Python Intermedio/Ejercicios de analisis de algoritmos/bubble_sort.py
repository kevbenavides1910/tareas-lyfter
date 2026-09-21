"""
Big O Analysis: O(n^2)

The outer loop runs n times, and for each outer iteration the inner
loop runs (almost) n times as well, giving roughly n * n comparisons.
This holds for the worst case (reverse-sorted list) and the average
case. Without an early-exit flag, it also holds for the best case
(already sorted list).
"""


def bubble_sort(numbers_list):
    n = len(numbers_list)
    for i in range(n):
        for j in range(n - i - 1):
            if numbers_list[j] > numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
    return numbers_list


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print(bubble_sort(sample))
