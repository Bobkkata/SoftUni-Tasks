wagons = int(input())
command = input()
train = [0] * wagons


while command != "End":
    action = command.split()[0]

    if action == "add":
        n_people = int(command.split()[1])
        train[-1] += n_people
    elif action == 'insert':
        index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[index] += n_people
    elif action == 'leave':
        index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[index] -= n_people
    command = input()

print(train)