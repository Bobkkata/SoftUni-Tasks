from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

matches = 0
worm_count = 0

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()
    worm_count += 1

    if worm <= 0:
        holes.appendleft(hole)
        continue
    elif worm == hole:
        matches += 1
        continue
    else:
        worm -= 3
        worms.append(worm)

if matches:
    print(f"Matches: {matches}")
elif not matches:
    print("There are no matches.")

if not worms and worm_count == matches:
    print("Every worm found a suitable hole!")
elif not worms and worm_count != matches:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if not holes:
    print("Holes left: none")
if holes:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")