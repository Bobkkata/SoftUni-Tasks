max_number = int(-99999999999)


while True:
    number = input()

    if number != 'Stop':
        number = int(number)
        if number > max_number:
            max_number = number

    elif number == 'Stop':
        print(max_number)
        break

