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

    height = len(grid)    # height of grid
    width = len(grid[0])  # width of grid
    perimeter = 0         # initial perimeter of island

    for row in range(height):
        for col in range(width):
            # Check if current cell is a 1
            if grid[row][col] == 1:

                # Check if cell is on the first row
                if row == 0:
                    perimeter += 1
                else:
                    # Check if cell above is a 0 and add 1 to perimeter
                    if grid[row - 1][col] == 0:
                        perimeter += 1

                # Check if cell is on the first column
                if col == 0:
                    perimeter += 1
                else:
                    # Check if previous cell is a 0 and add 1 to perimeter
                    if grid[row][col - 1] == 0:
                        perimeter += 1

                # Check if cell is on the last row
                if row == height - 1:
                    perimeter += 1
                else:
                    # Check if the cell below is a 0 and add 1 to perimeter
                    if grid[row + 1][col] == 0:
                        perimeter += 1

                # Check if cell is on the last column
                if col == width - 1:
                    perimeter += 1
                else:
                    # Check if the next cell is a 0 and add 1 to perimeter
                    if grid[row][col + 1] == 0:
                        perimeter += 1

    return perimeter
