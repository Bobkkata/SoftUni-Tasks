def print_number(nums):
    negative_numbers = sum([num for num in nums if num < 0])
    positive_numbers = sum([num for num in nums if num > 0])

    print(negative_numbers)
    print(positive_numbers)

    if abs(negative_numbers) > positive_numbers:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
print_number(numbers)