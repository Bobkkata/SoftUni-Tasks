cena_skumriq = float(input())
cena_caca = float(input())
kilo_palamud = float(input())
kilo_safrid = float(input())
kilo_midi = int(input())

cena_palamud = cena_skumriq + (cena_skumriq * 0.60)
sume_palamud = kilo_palamud * cena_palamud
cena_safrid = cena_caca + (cena_caca * 0.80)
sume_safrid = kilo_safrid * cena_safrid
sume_midi = kilo_midi * 7.50
account = sume_palamud + sume_safrid + sume_midi
print(f'{account: .2f}')
