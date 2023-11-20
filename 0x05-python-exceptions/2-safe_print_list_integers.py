#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elementscount = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                elementscount += 1
        print()
        return elementscount
    except IndexError:
        print()
        return elementscount
