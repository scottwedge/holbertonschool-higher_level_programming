#!/bin/usr/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupleA = list(tuple_a)
    tupleB = list(tuple_b)
    tupleA.extend([0, 0])
    tupleB.extend([0, 0])
    sumA = tupleA[0] + tupleB[0]
    sumB = tupleA[1] + tupleB[1]
    finalTuple = (sumA, sumB)
    return finalTuple
