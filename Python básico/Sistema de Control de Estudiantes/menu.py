"""
menu.py - Displays the main menu and handles option selection.
"""

MENU_OPTIONS = {
    "1": "Add students",
    "2": "View all students",
    "3": "View top 3 students",
    "4": "View overall grade average",
    "5": "Export data to CSV",
    "6": "Import data from CSV",
    "7": "Delete a student",
    "8": "View failing students",
    "9": "Exit",
}


def display_menu() -> None:
    """Print the main menu to the console."""
    print("\n" + "=" * 40)
    print("   🎓 Lyfter — Student Management System")
    print("=" * 40)
    for key, label in MENU_OPTIONS.items():
        print(f"  {key}. {label}")
    print("=" * 40)


def get_valid_option() -> str:
    """Prompt the user until they enter a valid menu option. Returns the chosen key."""
    while True:
        choice = input("Select an option: ").strip()
        if choice in MENU_OPTIONS:
            return choice
        print(f"  ❌ Invalid option. Please choose a number between 1 and {len(MENU_OPTIONS)}.")
