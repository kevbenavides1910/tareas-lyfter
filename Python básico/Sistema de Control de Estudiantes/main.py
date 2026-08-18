"""
main.py - Entry point for the Lyfter Student Management System.
"""

from menu import display_menu, get_valid_option
from actions import (
    add_students,
    display_all_students,
    display_top_3,
    display_overall_average,
    delete_student,
    display_failing_students,
)
from data import export_to_csv, import_from_csv


def run_program() -> None:
    """Main loop: show the menu and dispatch actions until the user exits."""
    students: list[dict] = []

    print("\nWelcome to the Lyfter General Studies Institute — Student System 🎓")

    while True:
        display_menu()
        choice = get_valid_option()

        if choice == "1":
            add_students(students)

        elif choice == "2":
         display_all_students(students)

        elif choice == "3":
            display_top_3(students)

        elif choice == "4":
            display_overall_average(students)

        elif choice == "5":
            if not students:
                print("\n⚠️  No students to export.")
            else:
                export_to_csv(students)

        elif choice == "6":
            imported = import_from_csv()
            if imported is not None:
                students = imported

        elif choice == "7":
            delete_student(students)

        elif choice == "8":
            display_failing_students(students)

        elif choice == "9":
            print("\nGoodbye! 👋\n")
            break


if __name__ == "__main__":
    run_program()
