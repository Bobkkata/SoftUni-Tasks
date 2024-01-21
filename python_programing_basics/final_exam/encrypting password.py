n = int(input())

for i in range(n):
    password = input()
    if password.count(">") != 1 or password.count("<") != 1:
        print("Try another password!")
        continue
    start_index = password.index(">") + 1
    end_index = password.index("<")
    if start_index >= end_index:
        print("Try another password!")
        continue
    middle = password[start_index:end_index]
    groups = middle.split("|")
    if len(groups) != 4:
        print("Try another password!")
        continue
    if any(len(g) != 3 for g in groups):
        print("Try another password!")
        continue
    if not (groups[0].isdigit() and groups[1].islower() and groups[2].isupper() and all(c not in "<$" for c in groups[3])):
        print("Try another password!")
        continue
    if password[:start_index-1] != password[end_index+1:]:
        print("Try another password!")
        continue
    encrypted_password = "".join(groups)
    print(f"Password: {encrypted_password}")
