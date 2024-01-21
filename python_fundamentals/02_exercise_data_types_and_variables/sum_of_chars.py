number_of_the_lines = int(input())

result = 0

for idx in range(number_of_the_lines):
    letter = input()
    letter_is_ord = ord(letter)
    result += letter_is_ord

print(f'The sum equals: {result}')