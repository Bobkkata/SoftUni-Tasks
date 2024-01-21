n = int(input())

usernames = set()

for _ in range(n):
    names = input()
    if names not in usernames:
        usernames.add(names)

print(*usernames, sep='\n')
