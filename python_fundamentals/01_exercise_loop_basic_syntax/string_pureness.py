number_of_word = int(input())

for _ in range(number_of_word):
    word = input()
    is_pure = True

    for ch in word:
        if ch == ',' or ch == '.' or ch == '_':
            is_pure = False

    if not is_pure:
        print(f'{word} is not pure!')
    else:
        print(f'{word} is pure.')
