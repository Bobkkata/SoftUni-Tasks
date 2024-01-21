def min_max_sum_of_numbers():
    numbers_as_int = []
    min_number = 0
    max_number = 0
    sum_of_numbers = 0

    for num in numbers:
        num_is_int = int(num)
        numbers_as_int.append(num_is_int)
        min_number = min(numbers_as_int)
        max_number = max(numbers_as_int)
        sum_of_numbers = sum(numbers_as_int)

    print(f'The minimum number is {min_number}')
    print(f'The maximum number is {max_number}')
    print(f'The sum number is: {sum_of_numbers}')


numbers = input().split()

min_max_sum_of_numbers()