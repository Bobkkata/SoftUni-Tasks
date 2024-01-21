import math

record_sec = float(input())
record_m = float(input())
time_sec_1m = float(input())

sec = record_m * time_sec_1m
water_resistance = math.floor(record_m / 15) * 12.5
total_time = sec + water_resistance

if record_sec <= total_time:
    time_needed = total_time - record_sec
    print(f'No, he failed! He was {time_needed:.2f} seconds slower.')

elif record_sec >= total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')