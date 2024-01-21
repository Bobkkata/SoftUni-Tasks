n = int(input())

tank = 0
for _ in range(n):
    liter = int(input())

    if tank + liter > 255:
        print(f'Insufficient capacity!')

    else:
        tank += liter
print(tank)