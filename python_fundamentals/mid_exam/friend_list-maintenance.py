friends = input().split(", ")
blacklisted = set()
lost = set()

while True:
    command = input().split()
    if command[0] == "Report":
        break

    if command[0] == "Blacklist":
        name = command[1]
        if name in friends:
            blacklisted.add(name)
            friends[friends.index(name)] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(friends):
            name = friends[index]
            if name == "Lost":
                continue

            if name != "Blacklisted" and name not in lost:
                lost.add(name)
                friends[index] = "Lost"
                print(f"{name} was lost due to an error.")

    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(friends):
            old_name = friends[index]
            friends[index] = new_name
            print(f"{old_name} changed his username to {new_name}.")

blacklisted_count = len(blacklisted)
lost_count = len(lost)
print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(" ".join(friends))