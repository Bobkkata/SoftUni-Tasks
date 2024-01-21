month = input()
night = int(input())

studio = 0
apartment = 0
discount = 0
price = 0

if month == 'May' or month == 'October':
    apartment = 65
    if night > 14:
        discount = 0.1
        price = night * apartment
        price = price - (price * discount)
        print(f'Apartment: {price:.2f} lv.')
    else:
        price = night * apartment
        print(f'Apartment: {price:.2f} lv.')
    studio = 50
    if night > 14:
        discount = 0.3
        price = night * studio
        price = price - (price * discount)
        print(f'Studio: {price:.2f} lv.')
    elif night > 7:
        discount = 0.05
        price = night * studio
        price = price - (price * discount)
        print(f'Studio: {price:.2f} lv.')
    else:
        price = night * studio
        print(f'Studio: {price:.2f} lv.')


elif month == 'June' or month == 'September':
    apartment = 68.70
    if night > 14:
        discount = 0.1
        price = night * apartment
        price = price - (price * discount)
        print(f'Apartment: {price:.2f} lv.')
    else:
        price = night * apartment
        print(f'Apartment: {price:.2f} lv.')

    studio = 75.20
    if night > 14:
        discount = 0.2
        price = night * studio
        price = price - (price * discount)
        print(f'Studio: {price:.2f} lv.')
    else:
        price = night * studio
        print(f'Studio: {price:.2f} lv.')

elif month == 'July' or month == 'August':
    apartment = 77
    if night > 14:
        discount = 0.1
        price = night * apartment
        price = price - (price * discount)
        print(f'Apartment: {price:.2f} lv.')
    else:
        price = night * apartment
        print(f'Apartment: {price:.2f} lv.')

    studio = 76
    price = night * studio
    print(f'Studio: {price:.2f} lv.')
