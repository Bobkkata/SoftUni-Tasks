def get_next_pos(command, row, col):
    if command == 'up':
        if row > 0:
            return row - 1, col
        else:
            return n - 1, col
    elif command == 'down':
        if row < n - 1:
            return row + 1, col
        else:
            return 0, col
    elif command == 'left':
        if col > 0:
            return row, col - 1
        else:
            return row, n - 1
    elif command == 'right':
        if col < n - 1:
            return row, col + 1
        else:
            return row, 0


n = int(input())

matrix = [list(input()) for x in range(n)]

row = 0
col = 0
tons = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] == "S":
            row = r
            col = c
            break
    break

command = input()


while command != "collect the nets":
    matrix[row][col] = "-"
    row, col = get_next_pos(command, row, col)
    symbol = matrix[row][col]

    if symbol.isdigit():
        tons += int(symbol)
    elif symbol == "W":
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
        exit()

    command = input()

matrix[row][col] = "S"

if tons >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - tons} tons of fish more.")

if tons > 0:
    print(f"Amount of fish caught: {tons} tons.")

for rows in matrix:
    print(*rows, sep='')