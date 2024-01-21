animals = {}
areas = {}

while True:
    command = input().split()

    if command[0] == "EndDay":
        break

    elif command[0] == "Add:":
        animal_name, food_quantity, area = command[1].split("-")
        food_quantity = int(food_quantity)

        if animal_name in animals:
            animals[animal_name] += food_quantity
        else:
            animals[animal_name] = food_quantity

        if area in areas:
            areas[area].append(animal_name)
        else:
            areas[area] = [animal_name]

    elif command[0] == "Feed:":
        animal_name, food = command[1].split("-")
        food = int(food)

        if animal_name in animals:
            animals[animal_name] -= food
            if animals[animal_name] <= 0:
                print(animal_name + " was successfully fed")
                del animals[animal_name]
                for area, animal_list in areas.items():
                    if animal_name in animal_list:
                        animal_list.remove(animal_name)
                        areas[area] = animal_list
            else:
                for area, animal_list in areas.items():
                    if animal_name in animal_list:
                        areas[area] = animal_list
        else:
            continue

hungry_animals_per_area = {}

print("Animals:")
for animal, food_quantity in sorted(animals.items()):
    print(animal + " -> " + str(food_quantity) + "g")

for area, animal_list in areas.items():
    hungry_animals = 0
    for animal in animal_list:
        if animal in animals and animals[animal] > 0:
            hungry_animals += 1
    if hungry_animals > 0:
        hungry_animals_per_area[area] = hungry_animals

print("Areas with hungry animals:")
for area, hungry_animals in sorted(hungry_animals_per_area.items()):
    print(area + ": " + str(hungry_animals))
