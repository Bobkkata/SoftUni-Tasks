n1 = int(input())
n2 = int(input())
symbol = input()

result = 0

if symbol == '+':
    result = n1 + n2
    if result % 2 == 0:
        print(f'{n1} {symbol} {n2} = {result} - even')
    else:
        print(f'{n1} {symbol} {n2} = {result} - odd')

if symbol == '-':
    result = n1 - n2
    if result % 2 == 0:
        print(f'{n1} {symbol} {n2} = {result} - even')
    else:
        print(f'{n1} {symbol} {n2} = {result} - odd')

if symbol == '*':
    result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} {symbol} {n2} = {result} - even')
    else:
        print(f'{n1} {symbol} {n2} = {result} - odd')

if symbol == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    elif result % 2 == 0:
        result = n1 / n2
        print(f'{n1} {symbol} {n2} = {result:.2f}')
    else:
        print(f'{n1} {symbol} {n2} = {result:.2f}')

if symbol == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    elif result % 2 == 0:
        result = n1 % n2
        print(f'{n1} {symbol} {n2} = {result}')
    else:
        print(f'Cannot divide {n1} by zero')