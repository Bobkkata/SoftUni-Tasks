def sum_of_all():
    if product == 'coffee':
        total_sum = 1.50 * count
        print(f'{total_sum:.2f}')
    elif product == 'water':
        total_sum = 1.00 * count
        print(f'{total_sum:.2f}')
    elif product == 'coke':
        total_sum = 1.40 * count
        print(f'{total_sum:.2f}')
    elif product == 'snacks':
        total_sum = 2.00 * count
        print(f'{total_sum:.2f}')


product = input()
count = int(input())

sum_of_all()