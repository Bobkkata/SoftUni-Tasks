n = int(input())
price = 0
flag = True
for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                price += 1
        flag = False
        if flag:
            break
    if flag:
        break
print(price)
