adj = (int(input())) * 100

time = 1030

if time + adj < 0000:
    print("Monday")
elif time + adj > 2400:
    print("Wednesday")
else:
    print("Tuesday")
