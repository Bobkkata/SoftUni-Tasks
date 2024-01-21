def even_number():
    for digit in numbers:
        num = int(digit)
        if num % 2 == 0:
            even.append(num)
    print(even)


numbers = input().split()
even = []

even_number()