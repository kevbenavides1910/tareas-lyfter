"""
actions.py - Core business logic for the student management system.
Handles adding, viewing, ranking, averaging, deleting, and reporting students.
"""

import re
from student import Student

PASSING_GRADE = 60
SUBJECTS = ["spanish", "english", "social_studies", "science"]
SUBJECT_LABELS = {
    "spanish": "Spanish",
    "english": "English",
    "social_studies": "Social Studies",
    "science": "Science",
}


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

def is_valid_name(name: str) -> bool:
    """Return True if the name is non-empty and contains only letters and spaces."""
    if not name.strip():
        return False
    return bool(re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ\s]+", name.strip()))


def is_valid_section(section: str) -> bool:
    """Return True if the section matches the pattern: 1-2 digits followed by one letter (e.g. 10A, 11B)."""
    return bool(re.fullmatch(r"\d{1,2}[A-Za-z]", section.strip()))


def student_exists(students: list, full_name: str, section: str) -> bool:
    """Return True if a student with the same name and section already exists."""
    name_lower = full_name.strip().lower()
    section_upper = section.strip().upper()
    return any(
        s.full_name.lower() == name_lower and s.section.upper() == section_upper
        for s in students
    )


def is_valid_grade(value: str) -> bool:
    """Return True if value can be parsed as a float between 0 and 100."""
    try:
        grade = float(value)
        return 0 <= grade <= 100
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def prompt_full_name() -> str:
    """Prompt the user for a valid full name."""
    while True:
        name = input("  Full name: ").strip()
        if is_valid_name(name):
            return name
        print("  ❌ Invalid name. It must not be empty and must contain only letters and spaces.")


def prompt_section() -> str:
    """Prompt the user for a valid section (e.g. 10A, 11B)."""
    while True:
        section = input("  Section (e.g. 10A, 11B): ").strip().upper()
        if is_valid_section(section):
            return section
        print("  ❌ Invalid section. Format must be 1–2 digits followed by one letter (e.g. 10A).")


def prompt_grade(subject_label: str) -> float:
    """Prompt the user for a valid grade (0–100) for the given subject."""
    while True:
        raw = input(f"  {subject_label} grade (0–100): ")
        if is_valid_grade(raw):
            return float(raw)
        print("  ❌ Invalid grade. Please enter a number between 0 and 100.")


# ---------------------------------------------------------------------------
# Core actions
# ---------------------------------------------------------------------------

def calculate_average(student: Student) -> float:
    """Calculate the grade average for a single student."""
    grades = [getattr(student, subject) for subject in SUBJECTS]
    return sum(grades) / len(grades)


def add_students(students: list) -> None:
    """Interactively add one or more students to the list."""
    while True:
        try:
            count = int(input("\nHow many students do you want to add? "))
            if count <= 0:
                print("  ❌ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("  ❌ Please enter a valid integer.")

    for i in range(1, count + 1):
        print(f"\n--- Student {i} of {count} ---")

        full_name = prompt_full_name()
        section = prompt_section()

        if student_exists(students, full_name, section):
            print(f"  ⚠️  A student named '{full_name}' in section '{section}' already exists. Skipping.")
            continue

        grades = {subject: prompt_grade(SUBJECT_LABELS[subject]) for subject in SUBJECTS}

        students.append(Student(
            full_name=full_name,
            section=section,
            **grades,
        ))
        print(f"  ✅ '{full_name}' added successfully.")


def display_all_students(students: list) -> None:
    """Print a formatted table of all students."""
    if not students:
        print("\n⚠️  No students have been added yet.")
        return

    print(f"\n{'#':<4} {'Name':<25} {'Section':<10} {'Spanish':>8} {'English':>8} {'Soc.St.':>8} {'Science':>8} {'Average':>8}")
    print("-" * 85)

    for idx, student in enumerate(students, start=1):
        avg = calculate_average(student)
        print(
            f"{idx:<4} {student.full_name:<25} {student.section:<10} "
            f"{student.spanish:>8.1f} {student.english:>8.1f} "
            f"{student.social_studies:>8.1f} {student.science:>8.1f} "
            f"{avg:>8.1f}"
        )


def display_top_3(students: list) -> None:
    """Print the top 3 students by average grade."""
    if not students:
        print("\n⚠️  No students have been added yet.")
        return

    ranked = sorted(students, key=calculate_average, reverse=True)
    top = ranked[:3]

    print("\n🏆 Top 3 Students by Average Grade")
    print("-" * 50)

    medals = ["🥇", "🥈", "🥉"]
    for rank, student in enumerate(top):
        avg = calculate_average(student)
        medal = medals[rank] if rank < len(medals) else f"#{rank + 1}"
        print(f"  {medal}  {student.full_name} ({student.section}) — Average: {avg:.2f}")


def display_overall_average(students: list) -> None:
    """Print each student's average and the overall average across all students."""
    if not students:
        print("\n⚠️  No students have been added yet.")
        return

    print(f"\n{'#':<4} {'Name':<25} {'Section':<10} {'Average':>8}")
    print("-" * 50)

    all_averages = []
    for idx, student in enumerate(students, start=1):
        avg = calculate_average(student)
        all_averages.append(avg)
        print(f"{idx:<4} {student.full_name:<25} {student.section:<10} {avg:>8.2f}")

    overall = sum(all_averages) / len(all_averages)
    print("-" * 50)
    print(f"\n📊 Overall average across all {len(students)} students: {overall:.2f}")


def delete_student(students: list) -> None:
    """Remove a student by full name and section after user confirmation."""
    if not students:
        print("\n⚠️  No students have been added yet.")
        return

    full_name = input("\n  Full name of student to delete: ").strip()
    section = input("  Section: ").strip().upper()

    match = next(
        (s for s in students if s.full_name.lower() == full_name.lower() and s.section.upper() == section),
        None,
    )

    if match is None:
        print(f"\n  ❌ No student named '{full_name}' in section '{section}' was found.")
        return

    confirm = input(f"\n  ⚠️  Are you sure you want to delete '{match.full_name}' ({match.section})? (yes/no): ").strip().lower()
    if confirm == "yes":
        students.remove(match)
        print(f"  ✅ '{match.full_name}' has been deleted.")
    else:
        print("  ℹ️  Deletion cancelled.")


def display_failing_students(students: list) -> None:
    """Print students who have at least one subject grade below the passing threshold."""
    if not students:
        print("\n⚠️  No students have been added yet.")
        return

    failing = []
    for student in students:
        failed_subjects = {
            SUBJECT_LABELS[subj]: getattr(student, subj)
            for subj in SUBJECTS
            if getattr(student, subj) < PASSING_GRADE
        }
        if failed_subjects:
            failing.append((student, failed_subjects))

    if not failing:
        print("\n✅ No students are currently failing any subject.")
        return

    print(f"\n❌ Failing Students (grade below {PASSING_GRADE})")
    print("-" * 55)

    for student, failed_subjects in failing:
        print(f"\n  👤 {student.full_name} — Section: {student.section}")
        for subject_label, grade in failed_subjects.items():
            print(f"      • {subject_label}: {grade:.1f}")
