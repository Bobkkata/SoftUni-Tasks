from collections import deque

material_of_crafting_toys = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

doll = 0
wooden_train = 0
teddy_bear = 0
bicycle = 0

while material_of_crafting_toys and magic_level:
    material = material_of_crafting_toys.pop()
    magic = magic_level.popleft()

    if material * magic == 150:
        doll += 1
        continue
    elif material * magic == 250:
        wooden_train += 1
        continue
    elif material * magic == 300:
        teddy_bear += 1
        continue
    elif material * magic == 400:
        bicycle += 1
        continue

    if material * magic < 0:
        material_of_crafting_toys.append(material + magic)
    elif material * magic > 0 and material * magic not in [150, 250, 300, 400]:
        material_of_crafting_toys.append(material + 15)
    elif material == 0 or magic == 0:
        if magic > 0 or magic < 0:
            magic_level.appendleft(magic)
        elif material > 0 or material < 0:
            material_of_crafting_toys.append(material)

if doll and wooden_train or teddy_bear and bicycle:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if material_of_crafting_toys:
    print(f"Materials left: {', '.join([str(x) for x in material_of_crafting_toys[::-1]])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

if bicycle > 0:
    print(f"Bicycle: {bicycle}")
if doll > 0:
    print(f"Doll: {doll}")
if teddy_bear > 0:
    print(f"Teddy bear: {teddy_bear}")
if wooden_train > 0:
    print(f"Wooden Train: {wooden_train}")