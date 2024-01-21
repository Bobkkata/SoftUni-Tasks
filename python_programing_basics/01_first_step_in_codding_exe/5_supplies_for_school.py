pen_number = int(input())
marker_number = int(input())
lt_preparations = int(input())
discount_percent = int(input())

discount = discount_percent / 100

packet_pen = 5.80
packet_marker = 7.20
preparations_for_lt = 1.20

price_for_pens = pen_number * packet_pen
price_for_marker = marker_number * packet_marker
price_for_preparations = lt_preparations * preparations_for_lt
price_for_all_materials = price_for_pens + price_for_marker + price_for_preparations

price_with_discount = price_for_all_materials - (price_for_all_materials * discount)

print(price_with_discount)


