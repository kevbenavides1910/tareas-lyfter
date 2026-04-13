import json
from pathlib import Path


# ── File path (always relative to this script, not the terminal's CWD) ────────
FILE_PATH = Path(__file__).parent / "pokemon.json"


def read_pokemons(file_path: Path) -> list[dict]:
    """Read the list of Pokémons from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_pokemons(file_path: Path, pokemons: list[dict]) -> None:
    """Save the list of Pokémons back to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=2, ensure_ascii=False)


def ask_integer(prompt: str) -> int:
    """Ask the user for an integer, retrying until a valid value is entered."""
    while True:
        raw = input(prompt)
        if raw.isdigit():
            return int(raw)
        print("  ⚠  Please enter a valid integer.")


def ask_types() -> list[str]:
    """Ask the user for one or more Pokémon types."""
    print("  (You can enter multiple types separated by commas, e.g.: Fire, Flying)")
    raw = input("  Type(s): ")
    return [t.strip() for t in raw.split(",") if t.strip()]


def build_pokemon() -> dict:
    """Collect all data for a new Pokémon from the user."""
    print("\n── Enter the new Pokémon's data ──")

    name   = input("  Name (English): ").strip()
    level  = ask_integer("  Level: ")
    types  = ask_types()

    print("  Base stats:")
    hp         = ask_integer("    HP: ")
    attack     = ask_integer("    Attack: ")
    defense    = ask_integer("    Defense: ")
    sp_attack  = ask_integer("    Sp. Attack: ")
    sp_defense = ask_integer("    Sp. Defense: ")
    speed      = ask_integer("    Speed: ")

    return {
        "name": {"english": name},
        "level": level,
        "type": types,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed,
        },
    }


def show_pokemon_summary(pokemon: dict) -> None:
    """Print a readable summary of a Pokémon."""
    name  = pokemon["name"]["english"]
    level = pokemon["level"]
    types = ", ".join(pokemon["type"])
    base  = pokemon["base"]
    print(f"\n  ✅ Pokémon added:")
    print(f"     Name  : {name}")
    print(f"     Level : {level}")
    print(f"     Type  : {types}")
    print(f"     Stats : HP {base['HP']} | ATK {base['Attack']} | DEF {base['Defense']}")
    print(f"             Sp.ATK {base['Sp. Attack']} | Sp.DEF {base['Sp. Defense']} | SPD {base['Speed']}")


def main() -> None:
    # 1. Read existing Pokémons from file
    pokemons = read_pokemons(FILE_PATH)
    print(f"📂 Loaded {len(pokemons)} Pokémon(s) from '{FILE_PATH.name}'.")

    # 2. Collect new Pokémon data from the user
    new_pokemon = build_pokemon()

    # 3. Append and save
    pokemons.append(new_pokemon)
    save_pokemons(FILE_PATH, pokemons)

    # 4. Confirm to the user
    show_pokemon_summary(new_pokemon)
    print(f"\n💾 '{FILE_PATH.name}' updated. Total: {len(pokemons)} Pokémon(s).\n")


if __name__ == "__main__":
    main()
