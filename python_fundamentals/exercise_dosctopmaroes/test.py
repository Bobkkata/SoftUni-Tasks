import re
from datetime import datetime, timedelta

food_pattern = r'(?:\||#)([a-zA-Z\s]+)(?:\||#)(\d{2}/\d{2}/\d{2})(?:\||#)(\d{1,5})(?:\||#)'

input_str = input()

food_matches = re.findall(food_pattern, input_str)

total_calories = 0

for match in food_matches:
    item_name, expiration_str, calories_str = match
    expiration_date = datetime.strptime(expiration_str, '%d/%m/%y')
    calories = int(calories_str)
    total_calories += calories
    print(f'Item: {item_name}, Best before: {expiration_str}, Nutrition: {calories}')

days_left = (total_calories // 2000)
print(f'You have food to last you for: {days_left} days!')