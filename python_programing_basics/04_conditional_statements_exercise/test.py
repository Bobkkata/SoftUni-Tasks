rec_in_sec = float(input())
space_m = float(input())
time_in_sec = float(input())

space_in_sec = space_m * time_in_sec
delay = round(space_m / 15)
delay_time = delay * 12.5
total_time = space_in_sec + delay_time
if rec_in_sec < total_time:
    total_time = abs(total_time - rec_in_sec)
    print(f'No, he failed! He was {total_time:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')