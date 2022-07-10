#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ade = len(tuple_a)
    bisi = len(tuple_b)

    sum1 = (tuple_a[0] if ade > 0 else 0) + (tuple_b[0] if bisi > 0 else 0)
    sum2 = (tuple_a[1] if ade > 1 else 0) + (tuple_b[1] if bisi > 1 else 0)

    return (sum1, sum2)
