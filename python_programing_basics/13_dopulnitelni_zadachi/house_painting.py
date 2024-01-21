#the height of the house
x = float(input())
#the lenght of a wall
y = float(input())
#height of the traingle
h = float(input())

#wall
side_wall = x * y
window = 1.5 * 1.5
both_sides_in_total = 2 * side_wall - 2 * window
back_wall = x * x
entrance = 1.2 * 2
front_and_rear = 2 * back_wall - entrance
total_area = both_sides_in_total + front_and_rear
green_paint = total_area / 3.4

#roof
the_two_rectangles = 2 * (x * y)
the_two_triangles = 2 * (x * h / 2)
tot_area = the_two_rectangles + the_two_triangles
red_paint = tot_area / 4.3

print(f'{green_paint: .2f}')
print(f'{red_paint: .2f}')