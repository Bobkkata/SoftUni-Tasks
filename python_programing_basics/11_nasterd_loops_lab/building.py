floors = int(input())
rooms = int(input())

type_fo_flat = ''
for f in range(floors, 0, -1):
    for a in range(rooms):
        flat_number = f * 10 + a

        if f == floors:
            type_fo_flat = f'L{flat_number}'
        elif f % 2 == 0:
            type_fo_flat = f'O{flat_number}'
        elif f % 2 != 0:
            type_fo_flat = f'A{flat_number}'
        print(type_fo_flat, end=' ')
    print()