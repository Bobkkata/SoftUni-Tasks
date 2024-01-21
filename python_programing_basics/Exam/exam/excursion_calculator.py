people = int(input())
season = input()

if people <= 5:
    if season == 'spring':
        price_for_one_people = 50.00
        total_sum = people * price_for_one_people
    elif season == 'summer':
        price_for_one_people = 48.50
        total_sum = people * price_for_one_people
    elif season == 'autumn':
        price_for_one_people = 60.00
        total_sum = people * price_for_one_people
    elif season == 'winter':
        price_for_one_people = 86.00
        total_sum = people * price_for_one_people
elif people > 5:
    if season == 'spring':
        price_for_one_people = 48.00
        total_sum = people * price_for_one_people
    elif season == 'summer':
        price_for_one_people = 45.00
        total_sum = people * price_for_one_people
    elif season == 'autumn':
        price_for_one_people = 49.50
        total_sum = people * price_for_one_people
    elif season == 'winter':
        price_for_one_people = 85.00
        total_sum = people * price_for_one_people

if season == 'summer':
    total_sum = total_sum * 0.85
elif season == 'winter':
    total_sum = total_sum * 1.08

print(f'{total_sum:.2f} leva.')