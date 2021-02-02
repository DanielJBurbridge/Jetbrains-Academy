score = int(input())
maximum = int(input())

percentage = score / maximum * 100

grade = "NO GRADE"

if percentage < 60:
    grade = "F"
elif percentage < 70:
    grade = "D"
elif percentage < 80:
    grade = "C"
elif percentage < 90:
    grade = "B"
else:
    grade = "A"

print(grade)
