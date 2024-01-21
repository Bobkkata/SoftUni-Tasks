w = int(input())
l = int(input())
n = int(input())

init_sum_word = input()
total_sum = 0
while init_sum_word != 'Done':

    init_sum_word = int(init_sum_word)
    full_sum = w * l * n
    total_sum += init_sum_word
    diff = abs(full_sum - total_sum)
    if init_sum_word == 'Done':
        break
    if total_sum > full_sum:
        break
    init_sum_word = input()
if init_sum_word == 'Done':
    print(f'{diff} Cubic meters left.')
elif total_sum > full_sum:
    print(f'No more free space! You need {diff} Cubic meters more.')
