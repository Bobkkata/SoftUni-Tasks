fruit = input()
day_of_week = input()
quantity = float(input())

if fruit == 'banana':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        fruit_price = 2.50
        price = quantity * fruit_price
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        fruit_price = 2.70
        price = quantity * fruit_price
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'apple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        fruit_price = 1.20
        price = quantity * fruit_price
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        fruit_price = 1.25
        price = quantity * fruit_price
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'orange':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        fruit_price = 0.85
        price = quantity * fruit_price
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        fruit_price = 0.90
        price = quantity * fruit_price
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'grapefruit':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        fruit_price = 1.45
        price = quantity * fruit_price
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        fruit_price = 1.60
        price = quantity * fruit_price
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'kiwi':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        fruit_price = 2.70
        price = quantity * fruit_price
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        fruit_price = 3.00
        price = quantity * fruit_price
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'pineapple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        fruit_price = 5.50
        price = quantity * fruit_price
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        fruit_price = 5.60
        price = quantity * fruit_price
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'grapes':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        fruit_price = 3.85
        price = quantity * fruit_price
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        fruit_price = 4.20
        price = quantity * fruit_price
        print(f'{price:.2f}')
    else:
        print('error')
else:
    print('error')