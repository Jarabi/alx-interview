#!/usr/bin/python3
"""
Lockboxes challenge
"""


def canUnlockAll(boxes):
    """
    Deteremines if all the boxes can be opened.

    Args:
        boxes (list of lists): The lockboxes and their
        respective keys

    Returns:
        bool: True if all boxes can be opened else False
    """

    box_count = len(boxes)

    # Capture all unlocked boxes
    unlocked = set()

    for idx, box in enumerate(boxes):
        if len(box) == 0 or idx == 0:
            unlocked.add(idx)

        for key in box:
            if key < box_count and key != idx:
                # Update unlocked boxes
                unlocked.add(key)

    return len(unlocked) == box_count
