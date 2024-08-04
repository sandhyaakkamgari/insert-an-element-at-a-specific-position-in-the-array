def insert_at_position(arr, element, position):
  """Inserts an element at a specific position in the array.

  Args:
    arr: The list to insert into.
    element: The element to insert.
    position: The index where the element should be inserted.

  Returns:
    The modified list.
  """
  arr.insert(position, element)
  return arr

# Example usage:
my_array = [1, 2, 3, 4]
new_array = insert_at_position(my_array, 10, 2)
print(new_array)