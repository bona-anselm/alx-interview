#!/usr/bin/python3
""" Defines canUnlockAll """


def canUnlockAll(boxes):
    """ A method that determines if all the boxes can be opened """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    boxes_to_unlock = [0]
    unlocked_boxes = set()

    while boxes_to_unlock:
        unlocked_box_index = boxes_to_unlock.pop()
        unlocked_boxes.add(unlocked_box_index)
        unlocked_box = boxes[unlocked_box_index]

        if not isinstance(unlocked_box, list):
            return False

        for key in unlocked_box:
            if key < len(boxes) and key not in boxes_to_unlock \
                    and key not in unlocked_boxes:
                boxes_to_unlock.append(key)

    return len(unlocked_boxes) == len(boxes)
