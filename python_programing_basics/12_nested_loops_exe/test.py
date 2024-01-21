movie_name = input()

students = 0
standards = 0
kids = 0
all_tickets = 0
total_tickets = 0

flag = False

while movie_name != 'Finish':
    capacity = int(input())
    ticket = input()

    while ticket != 'End':
        all_tickets += 1
        if ticket == 'student':
            students += 1
            total_tickets += 1
        elif ticket == 'standard':
            standards += 1
            total_tickets += 1
        elif ticket == 'kid':
            kids += 1
            total_tickets += 1
        elif ticket == 'Finish':
            flag = True
        if flag:
            break
        if all_tickets == capacity:
            break
        ticket = input()

    if flag:
        print(f'{movie_name} - {all_tickets / capacity * 100 :.2f}% full.')
        break

    print(f'{movie_name} - {all_tickets / capacity * 100 :.2f}% full.')
    all_tickets = 0
    movie_name = input()

print(f'Total tickets: {total_tickets}')

if total_tickets != 0:
    print(f'{students / total_tickets * 100 :.2f}% student tickets.')
    print(f'{standards / total_tickets * 100 :.2f}% standard tickets.')
    print(f'{kids / total_tickets * 100 :.2f}% kids tickets.')

