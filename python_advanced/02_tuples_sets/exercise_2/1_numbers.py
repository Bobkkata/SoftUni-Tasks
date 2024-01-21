seq_one = set([int(x) for x in input().split()])
seq_two = set([int(x) for x in input().split()])

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + ' ' + second_command

    if command == 'Add First':
        [seq_one.add(int(el)) for el in data]
    elif command == 'Add Second':
        [seq_two.add(int(el)) for el in data]
    elif command == 'Remove First':
        [seq_one.discard(int(el)) for el in data]
    elif command == 'Remove Second':
        [seq_two.discard(int(el)) for el in data]
    elif command == 'Check Subset':
        print(seq_one.issubset(seq_two) or seq_two.issubset(seq_one))

print(*sorted(seq_one), sep=', ')
print(*sorted(seq_two), sep=', ')