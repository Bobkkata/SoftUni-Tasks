projection = input()

student = 0
standard = 0
kid = 0
total_ticket = 0
count = 0

while projection != 'Finish':
    free_seats = int(input())
    ticket = input()
    count = 0

    while ticket != 'End' or ticket == 'Finish':

        if ticket == 'student':
            student += 1
            total_ticket += 1
            count += 1
        elif ticket == 'standard':
            standard += 1
            total_ticket += 1
            count += 1
        elif ticket == 'kid':
            kid += 1
            total_ticket += 1
            count += 1
        if ticket == 'Finish':
            break
        ticket = input()
    if ticket == 'End' or ticket == 'Finish':
        print(f'{projection} - {(count / free_seats) * 100:.2f}% full.')
    if ticket == 'Finish':
        break
    projection = input()

purcent_free_seats = (student / total_ticket) * 100
purcent_of_student = (student / total_ticket) * 100
purcent_of_standard = (standard / total_ticket) * 100
purcent_of_kid = (kid / total_ticket) * 100
print(f'Total tickets: {total_ticket}')
print(f'{purcent_of_student:.2f}% student tickets.')
print(f'{purcent_of_standard:.2f}% standard tickets.')
print(f'{purcent_of_kid:.2f}% kids tickets.')

