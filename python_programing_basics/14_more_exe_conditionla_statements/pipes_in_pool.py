v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

first_pipe = h * p1
second_pipe = h * p2
total = first_pipe + second_pipe
if total <= v:
    purcent = total / v
