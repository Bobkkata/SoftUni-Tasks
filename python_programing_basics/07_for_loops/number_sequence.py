import sys
number_of_line = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(number_of_line):
    number = int(input())

    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')