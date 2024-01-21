orders = int(input())

order_sum = 0
for _ in range(orders):
    price_per_caps = float(input())
    days = int(input())
    caps_per_day = int(input())

    if price_per_caps < 0.01 or caps_per_day > 100:
        continue

    if days < 1 or days > 31:
        continue

    if caps_per_day < 1 or caps_per_day > 2000:
        continue

    total_sum = price_per_caps * days * caps_per_day
    order_sum += total_sum

    print(f'The price for the coffee is: ${total_sum:.2f}')
print(f'Total: ${order_sum:.2f}')
