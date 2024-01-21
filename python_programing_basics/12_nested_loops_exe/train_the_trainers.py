judge = int(input())
presentation = input()

final_sum = 0
sum_grades = 0
grade = 0
grade_number = 0
while presentation != 'Finish':
    sum_grade_presentation = 0
    for jury in range(1, judge + 1):
        grade = float(input())
        grade_number += 1
        final_sum += grade
        sum_grade_presentation += grade
    average_grade = sum_grade_presentation / judge
    sum_grades += grade

    print(f'{presentation} - {average_grade:.2f}.')
    presentation = input()

    if presentation == 'Finish':
        final_sum = final_sum / grade_number
        print(f"Student's final assessment is {final_sum:.2f}.")