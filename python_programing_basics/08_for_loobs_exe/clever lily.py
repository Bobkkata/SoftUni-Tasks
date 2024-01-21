age = int(input())
washing_machine = float(input())
toys_price = int(input())

total_sum = 0
money = 10
toys = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        total_sum = total_sum + money
        total_sum = total_sum - 1
        money = money + 10
    else:
        toys = toys + 1

toys = toys * toys_price
full_sum = total_sum + toys
diff = 0
if full_sum >= washing_machine:
    diff = abs(full_sum - washing_machine)
    print(f'Yes! {diff:.2f}')
else:
    diff = abs(full_sum - washing_machine)
    print(f'No! {diff:.2f}')