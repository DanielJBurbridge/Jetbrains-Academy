# write your code here

# with open('salary.txt', 'w') as file:
#     file.write("1000\n")
#     file.write("2000\n")
#     file.write("3000\n")
#     file.write("4000\n")
#     file.write("5000\n")
#     file.write("6000\n")
#     file.write("7000\n")
#     file.write("8000\n")
#     file.write("9000\n")
#     file.write("10000\n")

with open('salary.txt', 'r', encoding='utf-8') as in_file, \
     open('salary_year.txt', 'w', encoding='utf-8') as out_file:
    for line in in_file:
        out_file.write(str(int(line.strip()) * 12)+'\n')
