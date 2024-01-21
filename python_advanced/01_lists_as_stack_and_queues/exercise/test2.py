brackets = input().split()

stack = []
opening_brackets = "({["
closing_brackets = ")}]"

for char in parentheses_sequence:
    if char in opening_brackets:
        stack.append(char)
    elif char in closing_brackets:
        if not stack:
            print("NO")
            break
        