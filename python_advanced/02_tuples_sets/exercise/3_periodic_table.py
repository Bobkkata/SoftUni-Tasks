n = int(input())

table = set()

for _ in range(n):
    for el in input().split():
        table.add(el)

print(*table, sep='\n')