budget_peter = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

sum_video_card = video_card * 250

price_processor = sum_video_card * 0.35
sum_processor = processor * price_processor

price_ram = sum_video_card * 0.1
sum_ram = ram * price_ram

total_price = sum_video_card + sum_processor + sum_ram

if video_card > processor:
    total_price = total_price - (total_price * 0.15)

end_sum = abs(total_price - budget_peter)

if total_price <= budget_peter:
    print(f'You have {end_sum:.2f} leva left!')
else:
    print(f'Not enough money! You need {end_sum:.2f} leva more!')