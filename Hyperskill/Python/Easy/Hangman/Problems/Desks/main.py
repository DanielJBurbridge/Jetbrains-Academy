# put your python code here

class_one_pop = int(input())
class_two_pop = int(input())
class_three_pop = int(input())

if class_one_pop % 2 != 0:
    class_one_pop += 1

if class_two_pop % 2 != 0:
    class_two_pop += 1

if class_three_pop % 2 != 0:
    class_three_pop += 1

tables_req = class_one_pop / 2 + class_two_pop / 2 + class_three_pop / 2

print(int(tables_req))
