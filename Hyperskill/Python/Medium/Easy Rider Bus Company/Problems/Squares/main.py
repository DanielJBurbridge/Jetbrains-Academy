n = int(input())


def squares():
    num = 1
    while True:
        yield num * num
        num += 1


# Don't forget to print out the first n numbers one by one here

squared_numbers = squares()

for i in range(n):
    print(next(squared_numbers))
