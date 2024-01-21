init_steps = input()
sum_steps = 0
while init_steps != 'Going home':
    steps = int(init_steps)
    sum_steps += steps

    if sum_steps >= 10000:
        break
    init_steps = input()

if init_steps == 'Going home':
    home_steps = int(input())
    sum_steps += home_steps

diff = abs(sum_steps - 10000)

if sum_steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')