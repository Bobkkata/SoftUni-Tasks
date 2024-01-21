month = input()
number_nights = int(input())

if month == "May" or month == 'October':
    studio = 50
    apartment = 65
    studio = studio * number_nights
    if number_nights > 14:
        studio = studio * 0.70
    elif number_nights > 7:
        studio = studio * 0.95
    apartment = apartment * number_nights
    if number_nights > 14:
        apartment = apartment * 0.90
    print(f'Apartment: {apartment:.2f} lv.')
    print(f'Studio: {studio:.2f} lv.')

elif month == "June" or month == 'September':
    studio = 75.20
    apartment = 68.70
    studio = studio * number_nights
    if number_nights > 14:
        studio = studio * 0.90
    apartment = apartment * number_nights
    if number_nights > 14:
        apartment = apartment * 0.90
    print(f'Apartment: {apartment:.2f} lv.')
    print(f'Studio: {studio:.2f} lv.')

elif month == "July" or month == 'August':
    studio = 76
    apartment = 77
    studio = studio * number_nights
    apartment = apartment * number_nights
    if number_nights > 14:
        apartment = apartment * 0.90

    print(f'Apartment: {apartment:.2f} lv.')
    print(f'Studio: {studio:.2f} lv.')