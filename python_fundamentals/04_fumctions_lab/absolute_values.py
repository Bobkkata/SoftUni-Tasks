number = input().split()
list_number = []

for num in number:
    list_number.append(abs(float(num)))

print(list_number)