import sys
n = int(input())

max_number = -sys.maxsize
total_sum = 0
diff = 0
for num in range(1, n + 1):
    number_in_line = int(input())

    if number_in_line > max_number:
        max_number = number_in_line

    total_sum = total_sum + number_in_line

other_num_sum = total_sum - max_number

if other_num_sum == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    diff = abs(other_num_sum - max_number)
    print(f'Diff = {diff}')