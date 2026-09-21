"""
Big O Analysis: O(n * m * p)

Three nested loops: for each element in list_a, the entire list_b is
traversed, and for each combination of those two, the entire list_c
is traversed. Total iterations equal n * m * p, where n, m, p are the
sizes of list_a, list_b, and list_c respectively. If all three lists
are of similar size n, this is often expressed as O(n^3).
"""


def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f'{element_a} {element_b} {element_c}')
    return result_list


if __name__ == "__main__":
    print(generate_list_trios([1, 2], ['a', 'b'], ['x', 'y']))
