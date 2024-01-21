animals = {}
areas = {}

while True:
    command = input()
    if command == "EndDay":
        break

    tokens = command.split("-")
    action = tokens[0]
    animal_name = tokens[1]

    if action == "Add":
        needed_food = int(tokens[2])
        area = tokens[3]
        if animal_name in animals:
            animals[animal_name]["needed_food"] += needed_food
        else:
            animals[animal_name] = {"needed_food": needed_food, "area": area}

        if area in areas:
            areas[area].append(animal_name)
        else:
            areas[area] = [animal_name]

    elif action == "Feed":
        food = int(tokens[2])
        if animal_name in animals:
            animals[animal_name]["needed_food"] -= food
            if animals[animal_name]["needed_food"] <= 0:
                print(f"{animal_name} was successfully fed")
                area = animals[animal_name]["area"]
                areas[area].remove(animal_name)
                del animals[animal_name]

animals_output = "Animals:\n"
for animal, data in animals.items():
    animals_output += f"{animal} -> {data['needed_food']}g\n"
print(animals_output.strip())

hungry_areas_output = "Areas with hungry animals:\n"
for area, animals_list in areas.items():
    hungry_animals = len([animal for animal in animals_list if animals[animal]["needed_food"] > 0])
    if hungry_animals > 0:
        hungry_areas_output += f"{area}: {hungry_animals}\n"
print(hungry_areas_output.strip())
