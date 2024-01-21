from collections import deque

numbers = deque(input().split(" "))

print(*reversed(numbers))