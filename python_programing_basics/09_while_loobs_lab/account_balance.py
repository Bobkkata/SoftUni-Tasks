current_sum = 0

while True:
    price = input()

    if price != 'NoMoreMoney':
        price = float(price)
        if price > 0:
            current_sum += price
            print(f'Increase: {price:.2f}')
        else:
            print('Invalid operation!')
            print(f'Total: {current_sum:.2f}')
            break

    elif price == 'NoMoreMoney':
        print(f'Total: {current_sum:.2f}')
        break
