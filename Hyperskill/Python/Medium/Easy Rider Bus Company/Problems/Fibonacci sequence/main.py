def fibonacci(n):
    sequence = [0, 1]
    i = 1
    while i <= n:
        if i == 1:
            yield 0
        elif i == 2:
            yield 1
        else:
            yield sequence[-2] + sequence[-1]
            sequence.append(sequence[-2] + sequence[-1])
        i += 1
