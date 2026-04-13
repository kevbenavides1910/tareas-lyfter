total_grades = int(input("Enter the number of grades: "))

current_grade_index = 1
passed_count = 0
failed_count = 0
passed_sum = 0
failed_sum = 0
total_sum = 0

while current_grade_index <= total_grades:
    print(f"Enter grade number {current_grade_index}:")
    current_grade = float(input())
    
    total_sum += current_grade
    
    if current_grade < 70:
        failed_count += 1
        failed_sum += current_grade
    else:
        passed_count += 1
        passed_sum += current_grade
    
    current_grade_index += 1

total_average = total_sum / total_grades

passed_average = passed_sum / passed_count if passed_count > 0 else 0
failed_average = failed_sum / failed_count if failed_count > 0 else 0

print("\n--- GRADES SUMMARY ---")
print(f"Passed grades: {passed_count}")
print(f"Average of passed grades: {passed_average:.2f}")

print(f"Failed grades: {failed_count}")
print(f"Average of failed grades: {failed_average:.2f}")

print(f"Total average: {total_average:.2f}")