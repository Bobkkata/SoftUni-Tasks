text = (input())
sume = 0
for i in range(len(text)):
    if text[i] == "a":
        sume += 1
    elif text[i] == 'e':
        sume += 2
    elif text[i] == "i":
        sume += 3
    elif text[i] == 'o':
        sume += 4
    elif text[i] == 'u':
        sume += 5

print(sume)