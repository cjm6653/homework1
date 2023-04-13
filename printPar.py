"""
Name: Connor McRoberts
id: cjm6653
date: 4/13/23
"""


def extraSpace(S, M, i, j):
    """
    hw5 #5(b)
    Calculates the extra space between the end of the words and the
    margin.

    :param S: An array of Strings
    :param M: The 'margin' (number of chars on one line)
    :param i: index of start of 'slice'
    :param j: index of end of 'slice
    :return: The space between the end of the words and the margin
    """

    total_len = 0
    for n in range(i, j):
        total_len += len(S[n])
        if total_len > M:
            return float('inf')

    return M - total_len


def badnessLine(S, M, i, j):
    """
    hw5 #5(d)
    the same thing as extraSpace but named differently
    (if this was intended to be something different please
    correct me, meant to see you in office hours)

    :param S: An array of string
    :param M: The 'margin'
    :param i: index of the start of the slice
    :param j: index of the end of the slice
    :return: The space between the end of the words and the margin
    """
    return extraSpace(S, M, i, j)


def minBad(S, M, i):
    """
    hw5 #5(g)
    Computes the minimum badness of a paragraph recursively

    :param S: An array of strings
    :param M: The margin
    :param i: index of the start of the slice (it goes till the end)
    :return: The greatest badness of a line in the best configuration
    """
    if i == len(S):  # last line
        return 0
    else:
        min_badness = float('inf')
        for j in range(i + 1, len(S) + 1):
            line_badness = badnessLine(S, M, i, j) ** 3 + minBad(S, M, j)
            if line_badness < min_badness:
                min_badness = line_badness
        return min_badness


def minBadDynamic(S, M):
    """
    hw5 #5(h)
    Uses dynamic programming to make a more efficient
    version of minBad by storing previously computed
    values in a array

    :param S: An array of strings
    :param M: The margin
    :return: The greatest badness of a line in the best configuration
    """
    n = len(S)
    bad_paragraph = [0] * (n+1)
    for i in range(n-1, -1, -1):    # go in reverse order
        min_badness = float('inf')
        for j in range(i+1, n+1):
            if badnessLine(S, M, i, j) == float('inf'):
                break
            line_badness = badnessLine(S, M, i, j)**3 + bad_paragraph[j]
            if line_badness < min_badness:
                min_badness = line_badness
        bad_paragraph[i] = min_badness

    return bad_paragraph[0]


def minBadDynamicChoice(S, M):
    """
    hw5 #5(i)
    :param S: An array of strings
    :param M: The margin requested by the client

    :return: An array 'choice' where choice[i] returns and the index of S
    where the next line starts
    """
    n = len(S)
    bad_paragraph = [0] * (n + 1)
    choice = [0]*(n+1)

    for i in range(n - 1, -1, -1):  # go in reverse order
        min_badness = float('inf')
        for j in range(i + 1, n + 1):
            if badnessLine(S, M, i, j) == float('inf'):
                break
            line_badness = badnessLine(S, M, i, j) ** 3 + bad_paragraph[j]
            if line_badness < min_badness:
                min_badness = line_badness
                choice[i] = j
        bad_paragraph[i] = min_badness

    return choice, bad_paragraph[0]


def printParagraph(S, M):
    """
    hw5 #5(i)
    Prints out the best configuration for a paragraph

    :param S: An array of strings
    :param M: The margin
    :return: null
    """
    choices, x = minBadDynamicChoice(S, M)

    i = 0
    while i < len(S):
        j = choices[i]
        print(' ' + S[i:j])
        i = j

