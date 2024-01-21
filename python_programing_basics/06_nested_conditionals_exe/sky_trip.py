days_stay = int(input())
type_of_room = input()
star = input()

discount = 0

if type_of_room == 'room for one person':
    if days_stay < 10:
        discount = 0
        night = days_stay - 1
        night = night * 18
        night = night - (discount * night)
    elif 10 < days_stay < 15:
        discount = 0
        night = days_stay - 1
        night = night * 18
        night = night - (discount * night)
    else:
        discount = 0
        night = days_stay - 1
        night = night * 18
        night = night - (discount * night)

elif type_of_room == 'apartment':
    if days_stay < 10:
        discount = 0.3
        night = days_stay - 1
        night = night * 25
        night = night - (discount * night)
    elif 10 < days_stay < 15:
        discount = 0.35
        night = days_stay - 1
        night = night * 25
        night = night - (discount * night)
    else:
        discount = 0.5
        night = days_stay - 1
        night = night * 25
        night = night - (discount * night)

elif type_of_room == 'president apartment':
    if days_stay < 10:
        discount = 0.1
        night = days_stay - 1
        night = night * 35
        night = night - (discount * night)
    elif 10 < days_stay < 15:
        discount = 0.15
        night = days_stay - 1
        night = night * 35
        night = night - (discount * night)
    else:
        discount = 0.2
        night = days_stay - 1
        night = night * 35
        night = night - (discount * night)

star_discount = 0
if star == 'positive':
    star_discount = 0.25
    night = night + (night * star_discount)
    print(f'{night:.2f}')
elif star == 'negative':
    star_discount = 0.1
    night = night - (night * star_discount)
    print(f'{night:.2f}')


