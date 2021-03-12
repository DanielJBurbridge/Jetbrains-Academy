def range_sum(numbers, start, end):
    valid_values = [num for num in numbers if start <= num <= end]
    return sum(valid_values)


input_numbers = [int(num) for num in input().split()]
a, b = [int(num) for num in input().split()]
print(range_sum(input_numbers, a, b))
