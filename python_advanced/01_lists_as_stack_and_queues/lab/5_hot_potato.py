from collections import deque

name = deque(input().split())
n_toss = int(input()) - 1

while len(name) > 1:
    name.rotate(-n_toss)
    removed_kid = name.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {name.popleft()}")