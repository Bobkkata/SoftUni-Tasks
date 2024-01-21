import math

serial_name = input()
episode_min = int(input())
break_time = int(input())

lunch = break_time / 8
relax_time = break_time / 4
remaining_time = break_time - lunch - relax_time

diff = abs(remaining_time - episode_min)
rounded_diff = math.ceil(diff)

if remaining_time >= episode_min:
    print(f'You have enough time to watch {serial_name} and left with {rounded_diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {rounded_diff} more minutes.")

