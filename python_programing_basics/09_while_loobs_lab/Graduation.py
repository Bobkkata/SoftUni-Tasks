name = input()
bad_grade = 0
classes = 0
total_grade = 0

while True:
    current_grade = float(input())
    if current_grade < 4:
        bad_grade += 1
        if bad_grade == 2:
            classes += 1
            print(f'{name} has been excluded at {classes} grade')
            break
    elif current_grade >= 4:
        total_grade += current_grade
        classes += 1
        if classes == 12:
            total_grade = total_grade / 12
            print(f'{name} graduated. Average grade: {total_grade:.2f}')
            break