n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    current_num = int(input())

    if current_num < 200:
        p1 += 1
    elif current_num <= 399:
        p2 += 1
    elif current_num <= 599:
        p3 += 1
    elif current_num <= 799:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

p1_purcent = (p1 / n) * 100
p2_purcent = (p2 / n) * 100
p3_purcent = (p3 / n) * 100
p4_purcent = (p4 / n) * 100
p5_purcent = (p5 / n) * 100

print(f'{p1_purcent:.2f}%')
print(f'{p2_purcent:.2f}%')
print(f'{p3_purcent:.2f}%')
print(f'{p4_purcent:.2f}%')
print(f'{p5_purcent:.2f}%')