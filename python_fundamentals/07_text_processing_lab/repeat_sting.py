words = input().split()
result = ''

for word in words:
    result += word * len(word)

# Лист компрехеншън
# [ word * len(word) for word in words]

print(result)