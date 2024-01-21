amount_of_nylon = int(input())
amount_of_paint = int(input())
amount_of_diluent = int(input())
time = int(input())

protective_nylon = 1.50 #лева за квадратен метър
paint = 14.50 #лв за литър
paint_thinner = 5.00 #лв за литър

discount = amount_of_paint * 0.10
bag = 0.40
nylon_m = 2

sume_nylon = (amount_of_nylon + nylon_m) * protective_nylon
sume_for_paint = (amount_of_paint + discount) * paint
sume_for_thinner = amount_of_diluent * paint_thinner

full_sume_for_material = sume_nylon + sume_for_paint + sume_for_thinner + bag
sume_for_master = (full_sume_for_material * 0.30) * time
final_sume = full_sume_for_material + sume_for_master

print(f'{final_sume}')
