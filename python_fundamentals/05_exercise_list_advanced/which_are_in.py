first = input().split(", ")
second = input().split(", ")

result = []

for substr in first:
    for word in second:
        found_substr = substr in word
        if found_substr:
            result.append(substr)
            break
print(result)
