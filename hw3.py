from collections import deque
"""
Name: Connor McRoberts
ID: cjm6653
"""


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def search(arr, val):
    """
    Problem #1, iterative binary search algorithm

    :param arr: an array of integer values
    :param val: the value we are searching for
    :return: A boolean
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Adjusts the middle value
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < val:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > val:
            high = mid - 1

        # If we reach here, arr[mid] == val
        else:
            return True

    # If we reach here, val is not present in array
    return False


def sortedHasSum(arr, x):
    """
    Problem #5(a), sortedHasSum

    :param arr: A SORTED array of integers
    :param x: A value we are looking at as the 'sum'
    :return: A boolean, true if found, false if not
    """

    left = 0
    right = len(arr) - 1

    while left <= right:

        twoSum = arr[left] + arr[right]

        if twoSum < x:
            left += 1
        elif twoSum > x:
            right -= 1
        else:
            return True

    return False


def hasSum(arr, x):
    """
    Problem #5(b), hasSum (not sorted)
    :param arr: A NON-SORTED array of integers
    :param x: A value we are looking at as the 'sum'
    :return: A boolean, true if found, false if not
    """

    # uses tim-sort, O(nlog(n)) time
    arr.sort()

    """
    Due to sortedHasSum()'s time-complexity being O(n), the final time-complexity
    of hasSum() is O(nlog(n) + n), which asymptotically is equal to O(nlog(n)).
    """
    return sortedHasSum(arr, x)


def Partition(arr, lowMark, highMark):
    pivot = arr[highMark]

    # Known in the slides as the slow mark in slides
    pIndex = lowMark

    # increment the slow mark and swap the elements when needed
    for i in range(lowMark, highMark):
        if arr[i] <= pivot:
            swap(arr, i, pIndex)
            pIndex += 1

    # swaps element at the 'pindex' with the pivot
    swap(arr, pIndex, highMark)

    # returns the index ofr the pivot element
    return pIndex


def quickSortHelp(arr, lowMark, highMark):

    stack = deque()

    stack.append((lowMark, highMark))

    # loop until stack is empty
    while stack:

        lowMark, highMark = stack.pop()

        pivot = Partition(arr, lowMark, highMark)

        if pivot - 1 > lowMark:
            stack.append((lowMark, pivot - 1))

        if pivot + 1 < highMark:
            stack.append((pivot + 1, highMark))


def quickSort(arr):
    """
    Problem #6
    An imperative form of quicksort such that the stack does not
    grow larger than log(n) size.
    Please view quickSortHelp(), Partition(), and swap() to see
    helper functions.
    :param arr: The array we are performing quickSort on.
    """
    quickSortHelp(arr, 0, len(arr) - 1)

