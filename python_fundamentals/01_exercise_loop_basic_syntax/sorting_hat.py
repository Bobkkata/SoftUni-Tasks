while True:
    name = input()
    if name == 'Welcome!':
        print(f'Welcome to Hogwarts.')
        break
    if name == 'Voldemort':
        print('You must not speak of that name!')
        break

    number = len(name)
    if number < 5:
        print(f'{name} goes to Gryffindor.')
    elif number == 5:
        print(f'{name} goes to Slytherin.')
    elif number == 6:
        print(f'{name} goes to Ravenclaw.')
    else:
        print(f'{name} goes to Hufflepuff.')