def quick_sort(array):
    # sort the array using the algorithm
    quick_sort_algorithm(array, 0, len(array) - 1)


# function to swap elements
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def quick_sort_algorithm(array, start, end):
    # base case: if the subarray has zero or one element, it is already sorted
    if start < end:
        # set pivot to second last element
        pivot = array[end - 1]
        # partition array and get the pivot index
        index = partition(array, start, end, pivot)
        # recursively sort left and right subarrays
        quick_sort_algorithm(array, start, index - 1)
        quick_sort_algorithm(array, index, end)


# function to provide the partition index
# and swap elements around the pivot
def partition(array, left, right, pivot):

    while left <= right:
        # move left index to the right until elements are less than the pivot
        while array[left] < pivot:
            left += 1

        # move right index to the left until elements are greater than the pivot
        while array[right] > pivot:
            right -= 1

        # swap elements at left and right indexes if they are in wrong order
        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1

    return left


#  list of words to be sorted
words = ["fig", "date", "banana", "cherry", "berry", "grape", "apple"]
print("Original list:", words)
quick_sort(words)
print("Sorted list:", words)
