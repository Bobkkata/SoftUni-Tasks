target_of_day = int(input())
total_money = 0
flag = True
action = input()
while action != 'closed':
    if action == 'closed':
        break
    if action == 'haircut':
        action_one = input()
        if action_one == 'mens':
            price = 15
            total_money += price
        elif action_one == 'ladies':
            price = 20
            total_money += price
        elif action_one == 'kids':
            price = 10
            total_money += price
    elif action == 'color':
        action_one = input()
        if action_one == 'touch up':
            price = 20
            total_money += price
        elif action_one == 'full color':
            price = 30
            total_money += price
    if total_money >= target_of_day:
        flag = False
    if not flag:
        break
    action = input()

if total_money >= target_of_day:
    print(f"You have reached your target for the day!")
    print(f"Earned money: {total_money}lv.")
elif total_money < target_of_day:
    diff = abs(target_of_day - total_money)
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {total_money}lv.")