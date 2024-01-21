message_sends = int(input())

for _ in range(message_sends):
    code_number = int(input())
    if code_number == 88:
        print(f'Hello')
    elif code_number == 86:
        print(f'How are you?')
    elif code_number != 88 and code_number < 88:
        print(f'GREAT!')
    elif code_number > 88:
        print(f'Bye.')