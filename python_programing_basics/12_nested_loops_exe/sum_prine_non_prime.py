command = input()

prime_number = 0
non_prime_number = 0
while command != 'stop':
    number = int(command)

    if number < 0:
        print('Number is negative.')
        command = input()
        continue

    count = 0
    for n in range(1, number + 1):
        if number % n == 0:
            count += 1

    if count == 2:
        prime_number += number
    else:
        non_prime_number += number
    command = input()

print(f'Sum of all prime numbers is:{prime_number}')
print(f'Sum of all non prime numbers is:{non_prime_number}')
