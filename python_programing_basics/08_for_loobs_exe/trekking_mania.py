groups = int(input())

musala = 0
monblan = 0
kilimajaro = 0
k2 = 0
everest = 0
people_sum = 0

for i in range(1, groups + 1):
    people = int(input())

    if people <= 5:
        musala += people
        people_sum += people
    elif 6 <= people <= 12:
        monblan += people
        people_sum += people
    elif 13 <= people <= 25:
        kilimajaro += people
        people_sum += people
    elif 26 <= people <= 40:
        k2 += people
        people_sum += people
    elif 41 <= people:
        everest += people
        people_sum += people


musala_purcent = (musala / people_sum) * 100
monblan_purcent = (monblan / people_sum) * 100
kilimajaro_purcent = (kilimajaro / people_sum) * 100
k2_purcent = (k2 / people_sum) * 100
everest_purcent = (everest / people_sum) * 100

print(f'{musala_purcent:.2f}%')
print(f'{monblan_purcent:.2f}%')
print(f'{kilimajaro_purcent:.2f}%')
print(f'{k2_purcent:.2f}%')
print(f'{everest_purcent:.2f}%')