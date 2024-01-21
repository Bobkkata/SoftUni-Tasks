meter_on_green = float(input())

price_for_green_land = meter_on_green * 7.61
discount = 0.18 * price_for_green_land
final_price = price_for_green_land - discount

print(f'The final price is: {final_price}')
print(f'The discout is: {discount}')
