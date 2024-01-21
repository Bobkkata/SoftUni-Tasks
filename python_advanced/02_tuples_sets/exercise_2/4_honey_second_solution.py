from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    bee = bees.popleft()
    nec = nectar.pop()

    if nec >= bee:
        symbol = symbols.popleft()

        if symbol == "/":
            if nec != 0:
                total_honey += abs(bee / nec)
                symbols.popleft()
        elif symbol == "*":
            total_honey += abs(bee * nec)

        elif symbol == "+":
            total_honey += abs(bee + nec)

        elif symbol == "-":
            total_honey += abs(bee - nec)

    else:
        bees.appendleft(bee)
print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")