n = int(input())
flag = True

for a in range(1, 9):
    for b in range(9, a, - 1):
        for c in range(0, 9):
            for d in range(9, c, - 1):

                plus = a + b + c + d
                multiplication = a * b * c * d
                if plus == multiplication and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    flag = False
                    break
                elif multiplication // plus == 3 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    flag = False
                    break
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            break
    if not flag:
        break
if flag:
    print("Nothing found")