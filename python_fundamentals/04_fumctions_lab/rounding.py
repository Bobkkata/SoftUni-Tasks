def rounded_num():
    for num in numbers:
        list_of_numbers.append(round(float(num)))
    print(list_of_numbers)


numbers = input().split()
list_of_numbers = []

rounded_num()