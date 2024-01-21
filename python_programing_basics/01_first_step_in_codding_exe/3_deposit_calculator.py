deposit = float(input())
months = int(input())
annual_rate = float(input())

per_year = deposit * (annual_rate / 100)
annual_per_moths = per_year / 12
all_sume = deposit + months * annual_per_moths
print(all_sume)
