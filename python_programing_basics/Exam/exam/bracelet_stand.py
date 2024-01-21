money_for_day_tereze = float(input())
money_of_day = float(input())
expenses_of_all_time = float(input())
price_of_gift = float(input())

save_money_pocket = 5 * money_for_day_tereze
money_save = 5 * money_of_day
total_save_money = save_money_pocket + money_save
expenses = total_save_money - expenses_of_all_time
diff = abs(expenses - price_of_gift)

if expenses > price_of_gift:
    print(f"Profit: {expenses:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")