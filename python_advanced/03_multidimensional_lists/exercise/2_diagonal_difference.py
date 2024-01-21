n = int(input())

matrix = [[int(x) for x in input().split()] for x in range(n)]

primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n)]

str_primary = sum([int(x) for x in primary])
str_secondary = sum([int(x) for x in secondary])

print(abs(str_primary - str_secondary))