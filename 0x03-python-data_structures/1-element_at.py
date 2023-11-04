#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return 'None'

    lenOfList = len(my_list)

    if idx > lenOfList:
        return 'None'

    return my_list[idx]
