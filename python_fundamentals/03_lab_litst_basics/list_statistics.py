n = int(input())

positive_number = []
negative_numbers = []
count_of_positive = 0
sum_of_negative = 0
for _ in range(n):
    random_numbers = int(input())
    if random_numbers > 0:
        count_of_positive += 1
        positive_number.append(random_numbers)
    else:
        sum_of_negative += random_numbers
        negative_numbers.append(random_numbers)
print(positive_number)
print(negative_numbers)
print(f'Count of positives: {count_of_positive}')
print(f'Sum of negatives: {sum_of_negative}')
