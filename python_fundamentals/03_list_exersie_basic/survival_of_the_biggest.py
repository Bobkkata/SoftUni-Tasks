numbers = [int(x) for x in input().split()]
count = int(input())

for _ in range(count):
    number_to_remove = min(numbers)
    numbers.remove(min(numbers))
print(','.join([str(x) for x in numbers]))