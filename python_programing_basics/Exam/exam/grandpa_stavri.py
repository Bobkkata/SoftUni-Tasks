n = int(input())
total_rakia = 0
sum_total_degree = 0
for n in range(1, n + 1):
    rakia_per_day = float(input())
    degree_of_rakia = float(input())

    total = rakia_per_day
    total_rakia += total

    total_degree = total * degree_of_rakia
    sum_total_degree += total_degree

total_sum = sum_total_degree / total_rakia

print(f'Liter: {total_rakia:.2f}')
print(f'Degrees: {total_sum:.2f}')
if total_sum < 38:
    print(f"Not good, you should baking!")
elif 38 < total_sum < 42:
    print(f"Super!")
else:
    print(f"Dilution with distilled water!")


