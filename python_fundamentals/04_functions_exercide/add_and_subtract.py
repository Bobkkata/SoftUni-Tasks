def add(a, b):
    return a + b


def subtract(c, d):
    return c - d


first = int(input())
second = int(input())
third = int(input())

add_result = add(first, second)
subtract_result = subtract(add_result, third)

print(subtract_result)
