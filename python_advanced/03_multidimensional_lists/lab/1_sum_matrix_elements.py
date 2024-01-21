row, col = [int(el) for el in input().split(', ')]

matrix = []
total_amount = 0

for i in range(row):
    row_data = [int(el) for el in input().split(', ')]
    matrix.append(row_data)
    total_amount += sum(row_data)

print(total_amount)
print(matrix)


#solution 2
# без total_amount

matrix = [[int(el) for el in input().split(', ')]for i in range(row)]

print(matrix)