"""
Name: Connor McRoberts
ID: cjm6653
date: 3/27/23
"""


def max2(a, b):
    """
    HW #1. computes the maximum of two numbers using bitwise
    operators.

    :param a: a 32-bit integer
    :param b: a 32-bit integer
    :return: a or b, dependent on which number is larger
    """
    c = a - b

    if 1 + (c >> 31):
        return a
    else:
        return b


def fSelect(arr, i):
    """
    HW #2. Functional recursive select algorithm

    :param arr: an unsorted array of integer
    :param i: the index of the nth largest element in the array
    :return: the nth largest element in the array
    """
    if len(arr) == 0:
        return -1

    x = arr[0]
    less = []
    same = []
    more = []
    for y in arr:
        if x < y:
            more.append(y)
        elif x > y:
            less.append(y)
        else:
            same.append(y)

    if i < len(less):
        return fSelect(less, i)
    elif i == len(less) | i < (len(less) + len(same)):
        return x
    else:
        return fSelect(more, i - (len(less) + len(same)))


def partition(arr, low, high):

    pivot = arr[high]  # pivot point
    i = low - 1  # slow mark
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def iSelectHelper(arr, k, low, high):
    # iterate loops over a smaller portion of the array,
    # partitioning it until it finds the element at k index
    while low <= high:

        pivotIndex = partition(arr, low, high)

        if pivotIndex == k:
            return arr[pivotIndex]

        elif pivotIndex > k:
            right = pivotIndex - 1

        else:
            left = pivotIndex + 1


def iSelect(arr, i):
    """
    HW #3: Iterative select sort, works by looping
    over a portion of the array and partitioning it
    into three separate parts. Greater than, equal to,
    and less than.

    :param arr: arr to select the i'th index from
    :param i: the index to be selected
    :return: returns the i + 1 smallest element in the array
    """
    if len(arr) == 0:
        return -1

    return iSelectHelper(arr, i, 0, len(arr) - 1)
