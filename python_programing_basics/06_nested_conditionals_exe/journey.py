budget = float(input())
season = input()

if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        budget = budget * 0.30
        print(f'{"Camp"} - {budget:.2f} ')
    elif season == 'winter':
        budget = budget * 0.70
        print(f'{"Hotel"} - {budget:.2f}')

elif budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        budget = budget * 0.40
        print(f'{"Camp"} - {budget:.2f} ')
    elif season == 'winter':
        budget = budget * 0.80
        print(f'{"Hotel"} - {budget:.2f}')

elif budget > 1000:
    print('Somewhere in Europe')
    if season == 'summer':
        budget = budget * 0.90
        print(f'{"Hotel"} - {budget:.2f} ')
    elif season == 'winter':
        budget = budget * 0.90
        print(f'{"Hotel"} - {budget:.2f}')