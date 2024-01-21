projection = input()
row = int(input())
collum = int(input())

price = 0
if projection == 'Premiere':
    price = 12
    total_price = price * row * collum
elif projection == 'Normal':
    price = 7.50
    total_price = price * row * collum
elif projection == 'Discount':
    price = 5
    total_price = price * row * collum
print(f'{total_price:.2f} leva')
