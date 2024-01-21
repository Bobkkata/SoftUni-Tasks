number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

deliver = 2.50


price_chicken_menu = number_chicken_menu * chicken_menu
price_fish_menu = number_fish_menu * fish_menu
price_vegetarian_menu = number_vegetarian_menu * vegetarian_menu
full_price_menu = price_chicken_menu + price_fish_menu + price_vegetarian_menu
desert_price = full_price_menu * 0.20

all_price = full_price_menu + desert_price  + deliver

print(f'{all_price}')