vacation_price = float(input())
money = float(input())

budget = money
spends = 0
days = 0
while True:
    action = input()
    amount = float(input())
    if action == 'spend':
        days += 1
        budget -= amount
        spends += 1
        if budget < 0:
            budget = 0

    elif action == 'save':
        spends = 0
        budget += amount
        days += 1

    if spends == 5:
        print(f"You can't save the money.")
        print(days)
        break
    if budget >= vacation_price:
        print(f'You saved the money for {days} days.')
        break