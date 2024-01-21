movie = input()
free_seats = int(input())

student = 0
standard = 0
kid = 0
seat_count = 0
total_ticket = 0
full_seat = free_seats


while movie != 'Finish':
    ticket = input()

    if movie == 'Finish' or movie == 'End':
        print(f'{movie} - {(seat_count / free_seats) * 100:.2f}% full.')

    if full_seat == 0:
        break
    if ticket == 'student':
        student += 1
        seat_count += 1
        total_ticket += 1
        full_seat -= 1
    elif ticket == 'standard':
        standard += 1
        seat_count += 1
        total_ticket += 1
        full_seat -= 1
    elif ticket == 'kid':
        kid += 1
        seat_count += 1
        total_ticket += 1
        full_seat -= 1
    ticket = input()
movie = input()

print(f'{student / total_ticket * 100 :.2f}% student tickets.')
print(f'{standard / total_ticket * 100 :.2f}% standard tickets.')
print(f'{kid / total_ticket * 100 :.2f}% kids tickets.')