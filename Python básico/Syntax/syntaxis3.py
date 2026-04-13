import random
secret_number = random.randint(1, 10)
print("¡Bienvenido al juego del número secreto!")
print("He pensado un número entre 1 y 10. ¡Intenta adivinarlo!")
user_guess = 0
while user_guess != secret_number:
    user_guess = int(input("Introduce tu número: "))
    if user_guess < secret_number:
        print("Demasiado bajo... ¡Prueba otra vez!")
    elif user_guess > secret_number:
        print("Demasiado alto... ¡Sigue intentando!")
    else:
        print(f"¡Felicidades! Adivinaste, el número era {secret_number}.")

print("Gracias por jugar.")
