def odd_and_even(number):
    for digit in single_number:
        num = int(digit)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    sum_of_odd_num = sum(odd)
    sum_of_even_num = sum(even)
    print(f'Odd sum = {sum_of_odd_num}, Even sum = {sum_of_even_num}')


single_number = input()

odd = []
even = []

odd_and_even(single_number)