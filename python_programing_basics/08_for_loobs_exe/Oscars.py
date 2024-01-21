actor = input()
init_point = float(input())
count_people = int(input())

total_point = init_point

for i in range(1, count_people + 1):
    name = input()
    point = float(input())

    current_point = (len(name) * point) / 2
    total_point = total_point + current_point

    if total_point >= 1250.5:
        break

if total_point < 1250.5:
    diff = 1250.5 - total_point
    print(f"Sorry, {actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_point:.1f}!")