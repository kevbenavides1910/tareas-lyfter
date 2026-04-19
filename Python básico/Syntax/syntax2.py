Name = input("Ingresa tu nombre: ")
Lastname = input("Ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))
if age < 0:
    category = "Edad no válida"
elif age <= 2:
    category = "un bebé"
elif age <= 11:
    category = "un niño"
elif age <= 13:
    category = "un preadolescente"
elif age <= 17:
    category = "un adolescente"
elif age <= 25:
    category = "un adulto joven"
elif age <= 64:
    category = "un adulto"
else:
    category = "un adulto mayor"
print(f"\nHola {Name} {Lastname}, basado en tu edad ({age} años), eres {category}.")