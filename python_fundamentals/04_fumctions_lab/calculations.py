def operator():
    if action == 'multiply':
        num = first_number * second_number
        print(num)
    elif action == 'divide':
        num = first_number // second_number
        print(num)
    elif action == 'add':
        num = first_number + second_number
        print(num)
    elif action == 'subtract':
        num = first_number - second_number
        print(num)


action = input()
first_number = int(input())
second_number = int(input())

operator()