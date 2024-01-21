animals = {}  # dictionary to store animals and their needed food
areas = {}  # dictionary to store areas and the hungry animals in them

while True:
    command = input()
    if command == "EndDay":
        break

    action, params = command.split(": ")
    animal_name, *other_params = params.split("-")
    quantity = int(other_params[0]) if other_params else None
    area = other_params[1] if len(other_params) > 1 else None

    if action == "Add":
        if animal_name in animals:
            animals[animal_name] += quantity
        else:
            animals[animal_name] = quantity

        if area in areas:
            areas[area].append(animal_name)
        else:
            areas[area] = [animal_name]

    elif action == "Feed":
        if animal_name in animals:
            if animals[animal_name] >= int(quantity):
                animals[animal_name] -= int(quantity)
                if animals[animal_name] == 0:
                    print(f"{animal_name} was successfully fed")
                    del animals[animal_name]
                    areas[area].remove(animal_name)
            else:
                print(f"{animal_name} was not fed")

        if area in areas and animal_name in areas[area]:
            if animal_name not in animals or animals[animal_name] <= 0:
                areas[area].remove(animal_name)

animals_output = "Animals:\n" + "\n".join([f"{animal_name} -> {animals[animal_name]}g" for animal_name in animals if animal_name in animals])
print(animals_output)

areas_output = "Areas with hungry animals:\n" + "\n".join([f"{area}: {len(areas[area])}" for area in areas if any([animals.get(animal_name, 0) > 0 for animal_name in areas[area]])])
print(areas_output)
