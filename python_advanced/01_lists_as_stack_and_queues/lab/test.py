from collections import deque

water = int(input())
name = input()

queue = deque()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        requester_liters = int(data[0])
        if requester_liters <= water:
            print(f"{queue.popleft()} got water")
            water -= requester_liters
        else:
            print(f"{queue.popleft()} must wait")
    elif len(data) == 2:
        _ , litter_to_add = data
        water += int(litter_to_add)
    command = input()

print(f"{water} liters left")