start = int(input())
finish = int(input())
magical = int(input())
counter = 0
flag = False
n = 0
for i in range(start, finish + 1):
    for k in range(start, finish + 1):
        counter += 1
        n = i + k
        if n == magical:
            print(f'Combination N:{counter} ({i} + {k} = {n})')
            flag = True
            break
    if flag:
        break
if not flag:
    print(f'{counter} combinations - neither equals {magical}')