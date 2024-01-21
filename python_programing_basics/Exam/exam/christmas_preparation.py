rolls_of_paper = int(input())
fabric_rolls = int(input())
liters_of_glue = float(input())
percent = int(input())

price_of_rolls_paper = rolls_of_paper * 5.80
price_of_fabric_rolls = fabric_rolls * 7.20
price_liters_of_glue = liters_of_glue * 1.20
total_sum = price_liters_of_glue + price_of_fabric_rolls + price_of_rolls_paper
discount = total_sum * percent / 100
discount_total_sum = total_sum - discount
print(f'{discount_total_sum:.3f}')
