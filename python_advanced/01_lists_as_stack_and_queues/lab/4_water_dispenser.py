from collections import deque

water = int(input())
name = input()

customers = deque()

while name != "Start":
    customers.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liter_requested = int(data[0])
        person = customers.popleft()

        if water >= liter_requested:
            print(f'{person} got water')
            water -= liter_requested
        else:
            print(f"{person} must wait")
    elif len(data) == 2:
        _ , litters_to_add = data
        water += int(litters_to_add)

    command = input()

print(f"{water} liters left")