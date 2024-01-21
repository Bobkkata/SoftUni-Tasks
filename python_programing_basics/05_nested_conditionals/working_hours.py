time = float(input())
day_of_week = input()

# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
# Sunday
if day_of_week == 'Monday':
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')

elif day_of_week == 'Tuesday':
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')

elif day_of_week == 'Wednesday':
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')

elif day_of_week == 'Thursday':
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Friday':
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Saturday':
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')
else:
    print('closed')