prime_numbers = []
tested_numbers = []

for i in range(2, 1001):
    if all(i % n != 0 for n in tested_numbers):
        prime_numbers.append(i)
    tested_numbers.append(i)




