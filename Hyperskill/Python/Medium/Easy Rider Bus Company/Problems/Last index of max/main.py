def last_indexof_max(numbers):
    max_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[max_index]:
            max_index = i

    return max_index
