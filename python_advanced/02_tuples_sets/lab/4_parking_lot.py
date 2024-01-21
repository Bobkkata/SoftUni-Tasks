n = int(input())

parking_cars = set()

for _ in range(n):
    command, cars_number = input().split(', ')

    if command == "IN":
        parking_cars.add(cars_number)
    elif command == "OUT":
        parking_cars.remove(cars_number)

if parking_cars:
    for car in parking_cars:
        print(car)
else:
    print(f"Parking Lot is Empty")