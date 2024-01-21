first_num = int(input())
second_num = int(input())

high_num = 0
for every_num in range(second_num + 1):
    if every_num % first_num == 0:
        high_num = every_num
print(high_num)