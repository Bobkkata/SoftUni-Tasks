n = int(input())


students_grades = {}

for _ in range(n):
    name, grade_as_str = input().split()
    grade = float(grade_as_str)

    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for name, grade in students_grades.items():
    avg_grade = sum(grade) / len(grade)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grade])}"
    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")
    