tabs_numbers = int(input())
salary = int(input())

for i in range(1, tabs_numbers + 1):
    current_tab = input()

    if current_tab == 'Facebook':
        salary = salary - 150
    elif current_tab == 'Instagram':
        salary = salary - 100
    elif current_tab == 'Reddit':
        salary = salary - 50
    if salary == 0:
        break
if salary == 0:
    print('You have lost your salary.')
else:
    print(salary)