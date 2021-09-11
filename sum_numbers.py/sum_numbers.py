def find_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print("Sum:", find_sum([4, 3, 2, 5, 7]))
# Sum: 21
