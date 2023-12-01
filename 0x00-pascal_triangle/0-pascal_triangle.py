#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """
    pascal_list = []
    cols = 1

    if n <= 0:
        return (pascal_list)

    for row in range(n):
        sub_list = []

        for col in range(cols):
            if row == 0 and col == 0:
                sub_list.append(1)
                break
            pre = 0 if col == 0 else pascal_list[row - 1][col - 1]
            next = 0 if col + 1 == cols else pascal_list[row - 1][col]
            sub_list.append(pre + next)
        cols += 1
        pascal_list.append(sub_list)
    return (pascal_list)
