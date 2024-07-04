def canUnlockAll(boxes):
    # Initialize a set to keep track of opened boxes
    opened = set()

    # A stack to manage boxes to open, start with the first box
    stack = [0]

    while stack:
        # Pop a box from the stack
        box_index = stack.pop()

        # If the box is already opened, continue to the next one
        if box_index in opened:
            continue
        # Mark the current box as opened
        opened.add(box_index)

        # Get the keys from the current box
        keys = boxes[box_index]

        for key in keys:
            if key not in opened:
                stack.append(key)
        
        # Check if all boxes have been opened
        return len(opened) == len(boxes)
    
    