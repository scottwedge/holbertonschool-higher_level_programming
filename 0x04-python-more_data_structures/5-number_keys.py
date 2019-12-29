#!/usr/bin/python3
def number_keys(my_dict):
    counter = 0
    for i in my_dict:
        if i in my_dict:
            counter += 1
    return counter
