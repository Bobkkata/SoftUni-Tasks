per_year = int(input())

basketball_shoes = per_year - (per_year * 0.40)
cloth = basketball_shoes - (basketball_shoes * 0.20)
bask_ball =  cloth / 4
accessories = bask_ball / 5
full_price = per_year + basketball_shoes + cloth + bask_ball + accessories
print(full_price)

