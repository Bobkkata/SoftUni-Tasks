from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque([int(x) for x in input().split()])
amount_of_fuel_needed = deque([int(x) for x in input().split()])

altitude_count = 0

while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
    fuel_quantity = initial_fuel.pop()
    consumption = additional_consumption_index.popleft()
    needed_fuel = amount_of_fuel_needed.popleft()

    amount = fuel_quantity - consumption

    if amount >= needed_fuel:
        altitude_count += 1
        print(f"John has reached: Altitude {altitude_count}")
    elif amount < needed_fuel:
        print(f"John did not reach: Altitude {altitude_count + 1}")
        break


if initial_fuel and altitude_count:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, altitude_count+1)])}")
elif initial_fuel and not altitude_count:
    print(f"John failed to reach the top.")
    print(f"John didn't reach any altitude.")

if not initial_fuel:
    print(f"John has reached all the altitudes and managed to reach the top!")