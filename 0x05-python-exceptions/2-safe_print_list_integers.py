#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elementscount = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                elementscount += 1
            except (ValueError, TypeError):
                pass
        print()
        return elementscount
    except IndexError:
        print()
        return elementscount
