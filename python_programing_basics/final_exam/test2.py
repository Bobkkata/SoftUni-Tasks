def print_animals(animals):
    print("Animals:")
    for animal, food in animals.items():
        print(f"{animal} -> {food}g")


def print_hungry_areas(animals, areas):
    hungry_areas = {}
    for animal, food in animals.items():
        if food > 0:
            area = areas[animal]
            if area not in hungry_areas:
                hungry_areas[area] = 1
            else:
                hungry_areas[area] += 1

    print("Areas with hungry animals:")
    for area, count in hungry_areas.items():
        print(f"{area}: {count}")


animals = {}
areas = {}

while True:
    command = input()
    if command == "EndDay":
        break

    tokens = command.split("-")
    animal_name = tokens[0].split(": ")[1]
    command_type = tokens[0].split(": ")[0]
    if command_type == "Add":
        needed_food_quantity = int(tokens[1])
        area = tokens[2]
        if animal_name not in animals:
            animals[animal_name] = needed_food_quantity
            areas[animal_name] = area
            if area not in areas:
                areas[area] = 1
            else:
                areas[area] += 1
        else:
            animals[animal_name] += needed_food_quantity
    elif command_type == "Feed":
        food = int(tokens[1])
        if animal_name in animals:
            animals[animal_name] -= food
            if animals[animal_name] <= 0:
                print(animal_name + " was successfully fed")
                areas[animal_name] = ""

                del animals[animal_name]
    else:
        continue

print_animals(animals)
print_hungry_areas(animals, areas)
