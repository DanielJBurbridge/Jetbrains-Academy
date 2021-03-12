# use the function blackbox(lst) that is already defined
my_list = [1, 2, 3]

if id(my_list) == id(blackbox(my_list)):
    print('modifies')
else:
    print('new')
