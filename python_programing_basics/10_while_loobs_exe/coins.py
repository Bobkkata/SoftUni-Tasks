from math import floor
coins = 0
coins_change = float(input())
change_coins = floor(coins_change * 100)
while True:
    if change_coins >= 200:
        change_coins -= 200
    elif change_coins >= 100:
        change_coins -= 100
    elif change_coins >= 50:
        change_coins -= 50
    elif change_coins >= 20:
        change_coins -= 20
    elif change_coins >= 10:
        change_coins -= 10
    elif change_coins >= 5:
        change_coins -= 5
    elif change_coins >= 2:
        change_coins -= 2
    elif change_coins >= 1:
        change_coins -= 1
    coins += 1
    if change_coins <= 0:
        print(coins)
        break