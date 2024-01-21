price_vegetables = float(input())
price_fruits = float(input())
total_price_vegetables = int(input())
total_price_fruits = int(input())

euro = 1.94

vegetables = price_vegetables * total_price_vegetables
fruit = price_fruits * total_price_fruits
total = vegetables + fruit
lv_to_euro = total / euro

print(f'{lv_to_euro: .2f}')