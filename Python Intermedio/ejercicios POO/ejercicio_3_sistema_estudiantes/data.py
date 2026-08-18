"""
data.py - Handles CSV export and import of student records.
"""

import csv
import os
from student import Student

CSV_FILENAME = os.path.join(os.path.dirname(__file__), "students.csv")
CSV_HEADERS = ["full_name", "section", "spanish", "english", "social_studies", "science"]


def export_to_csv(students: list) -> None:
    """Export the current list of students to a CSV file."""
    with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(student.to_dict() for student in students)

    print(f"\n✅ Data exported successfully to '{CSV_FILENAME}' ({len(students)} students).")


def import_from_csv() -> list | None:
    """
    Import student records from a CSV file.
    Returns the list of students or None if the file does not exist.
    """
    if not os.path.exists(CSV_FILENAME):
        print(f"\n⚠️  No exported file found ('{CSV_FILENAME}' does not exist).")
        return None

    students = []

    with open(CSV_FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(Student(
                full_name=row["full_name"],
                section=row["section"],
                spanish=float(row["spanish"]),
                english=float(row["english"]),
                social_studies=float(row["social_studies"]),
                science=float(row["science"]),
            ))

    print(f"\n✅ Data imported successfully from '{CSV_FILENAME}' ({len(students)} students).")
    return students
