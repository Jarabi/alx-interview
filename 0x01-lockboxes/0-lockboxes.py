#!/usr/bin/python3
""" Lockboxes challenge """


def canUnlockAll(boxes):
    """
    Deteremines if all the boxes can be opened.

    Args:
        boxes: A list of lists

    Returns:
        True if all boxes can be opened else False
    """

    # If there is only one box (boxes[0]), it is unlocked
    if not boxes or len(boxes) == 1:
        return True

    # Get all keys in current box in a set so there are no duplicates
    box_keys = set(boxes[0])

    # Capture all unlocked boxes
    unlocked_boxes = {0}

    # Initialize iterator with the index of the first unlocked box
    iterator = [0]

    while (iterator):
        # Get first index in the iterator
        current_box = iterator.pop(0)

        for key in boxes[current_box]:
            if key not in unlocked_boxes:
                # Update variables with new keys
                box_keys.add(key)
                unlocked_boxes.add(key)
                iterator.append(key)

    return len(unlocked_boxes) == len(boxes)
