my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair_list = []

for number in my_list:
    if number % 2 == 0:
        pair_list.append(number)

print(pair_list)