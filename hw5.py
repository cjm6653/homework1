"""
Name: Connor McRoberts
ID: cjm6653
date: 4/10/23
"""


def fibDyn(n):
    """
    #3 on HW5 make a dynamically allocated program to calculate
    the fibonacci sequence

    :param n: a natural number describing what you want from the
    fibonacci sequence
    :return: the nth number of the fibonacci sequence
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    arr = [0, 1]  # the original array of fibonacci numbers
    new = 0  # the next number in the fibonacci sequence
    i = 0  # iterator
    while i <= n - 2:
        new = arr[0] + arr[1]
        arr[0], arr[1] = arr[1], arr[0]
        arr[1] = new
        i += 1

    return arr[1]


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def knapSack(W, arr):
    """

    :param W: The maximum weight capacity of the bag
    :param arr: An array of items objects
    :return: The maximum value the knapsack can hold
    """
    sack = [[0 for x in range(W + 1)] for x in range(len(arr) + 1)]

    for i in range (len(arr) + 1):
        for w in range (W + 1):
            if i == 0 or w == 0:
                sack[i][w] = 0
            elif arr[i - 1].weight <= w:
                sack[i][w] = max(arr[i-1].value
                                 + sack[i-1][w - sack[i - 1].weight])
            else:
                sack[i][w] = sack[i-1][w]

    return sack[arr.legth][W]


def knapSackContents(W, arr):
    """

    :param W: The maximum weight capacity of the baf
    :param arr: An array of Item objects
    :return: A list of items that maximize the sacks value
    """
    # creation of dp matrix
    # sack[i][j] represents using the first i'th items with a capacity of j
    sack = [[0 for x in range(W + 1)] for x in range(len(arr) + 1)]

    for i in range(1, len(arr) + 1):
        for j in range(1, W + 1):
                if arr[i - 1][0] > j:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = max(arr[i-1][j],
                                    arr[i-1][i-arr[i-1].weight] + arr[i-1].value)

    # finds the items that maximize the sacks value from the matrix
    result = []
    m, n = len(arr), W
    while m > 0 and n > 0:
        if arr[m][n] != arr[m-1][n]:
            result.append(i-1)
            m -= arr[i-1][0]
        n -= 1

    # using the indexes of the array, we can gather the items that were added
    return [arr[i] for i in result]

