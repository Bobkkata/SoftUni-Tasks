budget = int(input())
season = input()
fishers = int(input())

price = 0

if season == 'Spring':
    price = 3000
    if fishers <= 6:
        price = price * 0.90
    elif 7 < fishers <= 11:
        price = price * 0.85
    elif fishers >= 12:
        price = price * 0.75

elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if fishers <= 6:
        price = price * 0.90
    elif 7 < fishers <= 11:
        price = price * 0.85
    elif fishers >= 12:
        price = price * 0.75

elif season == 'Winter':
    price = 2600
    if fishers <= 6:
        price = price * 0.90
    elif 7 < fishers <= 11:
        price = price * 0.85
    elif fishers >= 12:
        price = price * 0.75

if fishers % 2 == 0 and season != 'Autumn':
    price = price * 0.95

diff = abs(price - budget)
if budget >= price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')