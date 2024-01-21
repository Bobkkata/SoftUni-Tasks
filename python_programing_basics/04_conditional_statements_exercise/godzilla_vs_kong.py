money_for_film = float(input())
statists = int(input())
price_for_cloth_for_statists = float(input())

sum_for_decor = money_for_film * 0.1
sum_cloth = statists * price_for_cloth_for_statists
if statists > 150:
    sum_cloth = sum_cloth - (sum_cloth * 0.1)

final_price_film = sum_for_decor + sum_cloth

if money_for_film >= final_price_film:
    budget = money_for_film - final_price_film
    print(f'Action!')
    print(f'Wingard starts filming with {budget:.2f} leva left.')
else:
    budget = abs(final_price_film - money_for_film)
    print(f'Not enough money!')
    print(f'Wingard needs {budget:.2f} leva more.')

