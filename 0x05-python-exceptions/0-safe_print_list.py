#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elementsCount = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elementsCount += 1
        print()
        return elementsCount
    except IndexError:
        print()
        return elementsCount
