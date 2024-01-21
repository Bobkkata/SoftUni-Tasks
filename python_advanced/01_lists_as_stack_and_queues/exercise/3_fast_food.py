from collections import deque

food_per_day = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if food_per_day >= order:
        orders.popleft()
        food_per_day -= order
    else:
        print('Orders left:', *orders)
        break
else:
    print('Orders complete')