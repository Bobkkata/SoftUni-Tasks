number_of_lines = int(input())

total_sum = 0
total_sum2 = 0
for i in range(number_of_lines):
    number = int(input())
    total_sum = number + number
for i2 in range(number_of_lines):
    number2 = int(input())
    total_sum2 = number2 + number2


if total_sum == total_sum2:
    print(f'Yes, sum = {total_sum}')
else:
    diff = abs(total_sum - total_sum2)
    print(f'No, diff = {diff}')


