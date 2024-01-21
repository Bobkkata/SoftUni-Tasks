factor = int(input())
count = int(input())

result = []

for idx in range(1, count+1):
    result.append(idx * factor)
print(result)