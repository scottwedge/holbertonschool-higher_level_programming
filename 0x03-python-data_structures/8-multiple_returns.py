#!/bin/usr/python3
def multiple_returns(sentence):
    tuple_len = len(sentence)
    if tuple_len == 0:
        finalTuple = (0, None)
    else:
        finalTuple = (tuple_len, sentence[0])
    return finalTuple
