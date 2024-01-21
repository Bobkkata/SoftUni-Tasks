n = int(input())

for thousand in range(1, 10):
    for hundreds in range(1, 10):
        for ten in range(1, 10):
            for unit in range(1, 10):
                if n % thousand == 0 and n % hundreds == 0 and n % ten == 0 and n % unit == 0:
                    print(f'{thousand}{hundreds}{ten}{unit}', end=' ')