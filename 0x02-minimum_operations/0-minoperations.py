#!/usr/bin/python3
""" Defines minOperations """


def minOperations(n):
    """
        Calculates the fewest number of operations needed to result
        in exactly n H characters in the file
    """
    if n == 1:
        return 0

    total_ops = 0
    h = 1
    while h < n:
        if n % h == 0:
            h_copy = h
            total_ops += 1
        h += h_copy
        total_ops += 1

    if h == n:
        return total_ops
    else:
        return 0
