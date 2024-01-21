from math import floor

biscuits_per_worker = int(input())
workers_count = int(input())
competing_factory_production = int(input())

production = 0
for day in range(1, 31):
    daily_production = biscuits_per_worker * workers_count
    if day % 3 == 0:
        daily_production *= 0.75
    production += floor(daily_production)

print(f"You have produced {int(production)} biscuits for the past month.")

percentage = (abs(production - competing_factory_production) / competing_factory_production) * 100
if production > competing_factory_production:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")