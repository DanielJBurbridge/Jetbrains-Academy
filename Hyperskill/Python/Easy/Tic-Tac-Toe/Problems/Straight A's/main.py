# put your python code here

grades = input().split()
a_count = grades.count("A")
fraction = round(a_count / len(grades), 2)

print(fraction)
