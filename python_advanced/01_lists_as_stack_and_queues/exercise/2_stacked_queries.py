stack = []

for _ in range(int(input())):
    numbers = [int(x) for x in input().split()]
    command = numbers[0]

    if command == 1:
        stack.append(numbers[1])
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        print(max(stack))
    elif command == 4:
        print(min(stack))

stack.reverse()
print(*stack, sep=', ')
