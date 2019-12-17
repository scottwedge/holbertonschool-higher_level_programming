#!/bin/usr/python3
def max_integer(my_list=[]):
    lenList = len(my_list)
    if lenList == 0:
        return None
    for i in my_list:
        num = my_list[i]
        if num < my_list[i]:
            num = my_list[i]
        return num
