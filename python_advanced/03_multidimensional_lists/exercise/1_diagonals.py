n = int(input())

matrix = [[int(el) for el in input().split(', ')] for x in range(n)]

primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r1][n - r1 - 1] for r1 in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
