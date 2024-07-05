def canUnlockAll(boxes):
  """
  This function checks if all boxes can be opened using the given keys.

  Args:
      boxes: A list of lists, where each inner list represents the keys available in a box.

  Returns:
      True if all boxes can be opened, False otherwise.
  """

  # Initialize a set to track opened boxes efficiently
  opened_boxes = set([0])  # Box 0 is always opened

  # Iterate through each box's keys
  for box_num, keys in enumerate(boxes):
    # Check if the current box is already opened (avoid unnecessary processing)
    if box_num not in opened_boxes:
      continue

    # Add available keys to the opened_boxes set for future use
    opened_boxes.update(keys)

    # If all boxes are accounted for, return True early
    if len(opened_boxes) == len(boxes):
      return True

  # If the loop finishes without opening all boxes, return False
  return False