def bubble_sort(numbers):
    """Ordena una lista de menor a mayor, recorriendo de izquierda a derecha.
    Los elementos mayores 'burbujean' hacia el final."""
    n = len(numbers)
    for pass_number in range(n - 1):
        for index in range(n - 1 - pass_number):
            if numbers[index] > numbers[index + 1]:
                swap(numbers, index, index + 1)
    return numbers


def swap(numbers, first_index, second_index):
    """Intercambia dos elementos de una lista."""
    numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Ordenado:", bubble_sort(sample.copy()))
