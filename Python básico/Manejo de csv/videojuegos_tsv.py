import csv

FIELDS = ["nombre", "genero", "desarrollador", "clasificacion"]
OUTPUT_FILE = "videojuegos.tsv"


def get_game_count():
    while True:
        try:
            count = int(input("¿Cuántos videojuegos desea ingresar? "))
            if count > 0:
                return count
            print("Ingrese un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


def collect_game_data(index):
    print(f"\n--- Videojuego #{index} ---")
    return {
        "nombre": input("  Nombre: "),
        "genero": input("  Género: "),
        "desarrollador": input("  Desarrollador: "),
        "clasificacion": input("  Clasificación ESRB (E, T, M, etc.): "),
    }


def save_to_tsv(games, filepath):
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(games)


def main():
    count = get_game_count()

    games = [collect_game_data(i + 1) for i in range(count)]

    save_to_tsv(games, OUTPUT_FILE)
    print(f'\n✅ Archivo "{OUTPUT_FILE}" guardado con {count} videojuego(s).')


if __name__ == "__main__":
    main()
