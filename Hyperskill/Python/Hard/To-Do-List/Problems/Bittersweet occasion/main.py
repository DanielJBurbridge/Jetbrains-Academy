# finish the function
def find_the_parent(child):
    parents = [Drinks, Pastry, Sweets]

    for parent in parents:
        if issubclass(child, parent):
            print(parent.__name__)
