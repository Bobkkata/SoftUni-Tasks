stack = []
opening_brackets = "({["
closing_brackets = ")}]"

# Reading input from the user
parentheses_sequence = input().strip()

for char in parentheses_sequence:
    if char in opening_brackets:
        stack.append(char)
    elif char in closing_brackets:
        if not stack:
            print("NO")
            exit()
        top = stack.pop()
        if opening_brackets.index(top) != closing_brackets.index(char):
            print("NO")
            exit()

print("YES" if not stack else "NO")