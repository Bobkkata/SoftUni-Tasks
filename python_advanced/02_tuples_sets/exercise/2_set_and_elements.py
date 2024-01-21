n, m = [int(x) for x in input().split()]

first_num = {input() for _ in range(n)}
second_num = {input() for _ in range(m)}

print(*first_num & second_num, sep='\n')
