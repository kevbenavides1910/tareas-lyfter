first_number = float(input("Escribe el primer número: "))
second_number = float(input("Escribe el segundo número: "))
third_number = float(input("Escribe el tercer número: "))

if first_number >= second_number and first_number >= third_number:
    mayor = first_number
elif second_number >= first_number and second_number >= third_number:
    mayor = second_number
else:
    mayor = third_number

print(f"El número mayor es: {mayor}")