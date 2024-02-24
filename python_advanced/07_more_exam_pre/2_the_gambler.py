def get_next_pos(command, row, col):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


size = int(input())
matrix = [list(input()) for x in range(size)]

amount = 0
gambler_row = 0
gambler_col = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "G":
            amount += 100
            gambler_row = r
            gambler_col = c
            break


command = input()
while command != "end":
    matrix[gambler_row][gambler_col] = "-"
    gambler_row, gambler_col = get_next_pos(command, gambler_row, gambler_col)

    if matrix[gambler_row][gambler_col] == "-":
        command = input()
        continue
    elif matrix[gambler_row][gambler_col] == "W":
        amount += 100
    elif matrix[gambler_row][gambler_col] == "P":
        amount -= 200
        if amount <= 0:
            break
    elif matrix[gambler_row][gambler_col] == "J":
        amount += 100000
        print(f"You win the Jackpot!")
        break
    elif 0 <= gambler_row < size or 0 <= gambler_col < size or amount <= 0:
        print(f"Game over! You lost everything!")
        exit()

    command = input()

matrix[gambler_row][gambler_col] = "G"

if amount < 0:
    print(f"Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {amount}$")
    for rows in matrix:
        print(*rows, sep='')

