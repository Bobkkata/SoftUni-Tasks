n = int(input())
word = input()
list_with_word = []
all_list = []
for _ in range(n):
    words_of = input()

    all_list.append(words_of)
    if word in words_of:
        list_with_word.append(words_of)

print(all_list)
print(list_with_word)