trip = float(input())
puzzel = int(input())
dolls = int(input())
teddys = int(input())
minions = int(input())
trucks = int(input())

total_sum = (puzzel * 2.60) + (dolls * 3) + (teddys * 4.10) + (minions * 8.20) + (trucks * 2)
toys = puzzel + dolls + teddys + minions + trucks

if toys >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)

diff = abs(trip - total_sum)

if trip <= total_sum:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
