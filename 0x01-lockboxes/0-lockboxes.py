#!/usr/bin/python3
"""
There are n number of locked boxes
Each box is numbered in order
from 0 to n - 1
each box may hold keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
     method determines if all the boxes have keys to open them.

    :param boxes:
    :return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
