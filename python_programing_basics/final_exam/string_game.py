input_str = input()

while True:
    command = input().split()

    if command[0] == "Done":
        break

    elif command[0] == "Change":
        char, replacement = command[1], command[2]
        input_str = input_str.replace(char, replacement)
        print(input_str)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in input_str:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        substring = command[1]
        if input_str.endswith(substring):
            print("True")
        else:
            print("False")

    elif command[0] == "Uppercase":
        input_str = input_str.upper()
        print(input_str)

    elif command[0] == "FindIndex":
        char = command[1]
        index = input_str.find(char)
        print(index)

    elif command[0] == "Cut":
        start_index, count = int(command[1]), int(command[2])
        cut_str = input_str[start_index:start_index+count]
        print(cut_str)