# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     row = (int(x) for x in input().split(', '))
#     sub_list = []
#     for i in row:
#         if i % 2 == 0:
#             sub_list.append(i)
#     matrix.append(sub_list)
#
# print(matrix)

#solution 2
n = int(input())

matrix = []

for i in range(n):
    data = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    matrix.append(data)

print(matrix)