#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()

    total = 0

    for element in my_list:
        if element not in unique_integers:
            unique_integers.add(element)
            total += element

    return total
