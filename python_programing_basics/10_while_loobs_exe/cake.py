length = int(input())
width = int(input())
cake_number = length * width
init_part = input()
while init_part != 'STOP':
    part = int(init_part)
    cake_number -= part
    if cake_number <= 0:
        break
    init_part = input()
diff = abs(cake_number)
if init_part == 'STOP':
    print(f'{diff} pieces are left.')
if cake_number <= 0:
    print(f'No more cake left! You need {diff} pieces more.')