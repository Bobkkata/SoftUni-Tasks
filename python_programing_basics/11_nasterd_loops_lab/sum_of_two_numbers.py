start = int(input())
finish = int(input())
magical = int(input())
counter = 0
flag = False

for a in range(start, finish + 1):
    for b in range(start, finish + 1):
        counter += 1

        if a + b == magical:
            print(f'Combination N:{counter} ({a} + {b} = {magical})')
            flag = True
            if flag:
                break
    if flag:
        break
if not flag:
    print(f'{counter} combinations - neither equals {magical}')