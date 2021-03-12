# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
passwords.sort(key=len)

for password in passwords:
    print(password, len(password))
