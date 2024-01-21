import math

tournaments = int(input())
init_points = int(input())

stage_points = 0
points = 0
wins = 0

for i in range(1, tournaments + 1):
    stage = input()

    if stage == 'W':
        stage_points = 2000
        wins += 1
    elif stage == 'F':
        stage_points = 1200
    elif stage == 'SF':
        stage_points = 720

    points = points + stage_points
    full_sum = points + init_points
points = points / tournaments
purcent = (wins / tournaments) * 100
points = math.floor(points)

print(f'Final points: {full_sum}')
print(f'Average points: {points}')
print(f'{purcent:.2f}%')
