number = float(input())

if number == 0:
    print(f'zero')
if number > 0:
    if number > 1000000:
        print(f'large positive')
    elif number < 1:
        print(f'small positive')
    else:
        print(f'positive')
elif number < 0:
    if number < -1000000:
        print(f'large negative')
    elif number > -1:
        print(f'small negative')
    else:
        print(f'negative')