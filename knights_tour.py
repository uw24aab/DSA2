def partition(arr, low, high):
  """
  Partitions the given array around a pivot.

  Args:
    arr: The list to be partitioned.
    low: The starting index of the subarray.
    high: The ending index of the subarray.

  Returns:
    The index of the pivot after partitioning.
  """
  pivot = arr[high - 1]  # Pivot is the second-to-last element
  print("Pivot:", pivot)
  i = low - 1

  for j in range(low, high - 1):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high - 1] = arr[high - 1], arr[i + 1]
  return i + 1

def quick_sort(arr, low=0, high=None):
  """
  Sorts the given array using the QuickSort algorithm with a separate partition function.

  Args:
    arr: The list to be sorted.
    low: The starting index of the subarray (default: 0).
    high: The ending index of the subarray (default: length of the array).

  Returns:
    The sorted list.
  """
  if high is None:
    high = len(arr)

  if low < high - 1:  # Base case: subarray has at least 2 elements
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi)
    quick_sort(arr, pi + 1, high)

  return arr

# Test the quick_sort function
unsorted_array = [2, 3, 6, 8, 10, 11, 1]
sorted_array = quick_sort(unsorted_array)
print("Sorted array:", sorted_array)  # Output: Sorted array: [1, 2, 3, 6, 8, 10, 11]