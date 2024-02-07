#!/usr/bin/python3
"""
Island perimeter
"""


def island_perimeter(grid):
    """
    Returns the primeter of the island described in "grid"

    Args:
        grid (list): list of list of integers

    Returns:
        Perimeter of island described by grid or nothing (0)
    """

    rows = len(grid)
    cols = len(grid[0])
    ones = 0

    grid_perimeter = (rows + cols) * 2

    for row in grid:
        for col in range(cols):
            if col == 1:
                ones += 1i

    if ones == 0:
        return ones

    return grid_perimeter - (ones * 2)
