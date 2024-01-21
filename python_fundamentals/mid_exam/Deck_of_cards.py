cards = input().split(", ")
num_commands = int(input())

for i in range(num_commands):
    command = input().split(", ")
    action = command[0]
    card = command[1]

    if action == "Add":
        if card in cards:
            print("Card is already in the deck")
        else:
            cards.append(card)
            print("Card successfully added")
    elif action == "Remove":
        if card in cards:
            cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        index = int(card)
        if index < 0 or index >= len(cards):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")
    elif action == "Insert":
        index = int(command[1])
        if index < 0 or index >= len(cards):
            print("Index out of range")
        elif card in cards:
            print("Card is already added")
        else:
            cards.insert(index, card)
            print("Card successfully added")

print(", ".join(cards))