number_string = input().split()
result = []

for num in number_string:
    num = int(num)
    result.append(-num)

print(result)