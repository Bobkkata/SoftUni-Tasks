encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break

    instructions = command.split("|")

    if instructions[0] == "Move":
        num_letters = int(instructions[1])
        encrypted_message = encrypted_message[num_letters:] + encrypted_message[:num_letters]

    elif instructions[0] == "Insert":
        index = int(instructions[1])
        value = instructions[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif instructions[0] == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")