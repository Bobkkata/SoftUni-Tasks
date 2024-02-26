n = int(input())


def print_upper(n):
    for rows in range(0, n + 1):
        print(f" " * (n-rows), "* "*rows)


def print_bottom(n):
    for rows in range(n-1, 0, -1):
        print(f" " * (n-rows), "* "*rows)


print_upper(n)
print_bottom(n)