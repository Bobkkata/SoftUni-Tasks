min_number = int(99999999999)


while True:
    number = input()

    if number != 'Stop':
        number = int(number)
        if number < min_number:
            min_number = number

    elif number == 'Stop':
        print(min_number)
        break

