bad_grade = int(input())

grade_sume = 0
final_sum = 0
number_of_task = 0
problems = 0
worst_grade = 0
flag = False

init_task = input()
while init_task != 'Enough':
    task = init_task
    problems += 1
    number_of_task += 1
    grade = int(input())

    grade_sume += grade
    final_sum = grade_sume / number_of_task
    if grade <= 4:
        worst_grade += 1
    if worst_grade == bad_grade:
        flag = True
        break

    init_task = input()
if flag:
    print(f'You need a break, {worst_grade} poor grades.')

else:
    print(f'Average score: {final_sum:.2f}')
    print(f'Number of problems: {problems}')
    print(f'Last problem: {task}')
