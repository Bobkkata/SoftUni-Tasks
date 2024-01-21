length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
occupied_space = volume / 1000
liters_needed = percent * 0.01
needed_liters = occupied_space * (1 - liters_needed)
print(needed_liters)
