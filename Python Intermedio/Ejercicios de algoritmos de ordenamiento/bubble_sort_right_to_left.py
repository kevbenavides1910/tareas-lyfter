def bubble_sort_right_to_left(numbers):
    """Ordena una lista de menor a mayor, recorriendo de derecha a izquierda.
    Los elementos menores 'burbujean' hacia el inicio."""
    n = len(numbers)
    for pass_number in range(n - 1):
        for index in range(n - 1, pass_number, -1):
            if numbers[index] < numbers[index - 1]:
                swap(numbers, index, index - 1)
    return numbers


def swap(numbers, first_index, second_index):
    """Intercambia dos elementos de una lista."""
    numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Ordenado:", bubble_sort_right_to_left(sample.copy()))
