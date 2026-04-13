numbers = []

for i in range(10):
    current_number = int(input(f"Enter number {i+1}: "))
    numbers.append(current_number)

highest_number = numbers[0]

for num in numbers:
    if num > highest_number:
        highest_number = num

print(f"List of numbers: {numbers}")
print(f"The highest was {highest_number}.")