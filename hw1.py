"""
Name: Connor McRoberts
Student ID: 362004866
"""


def head(lst):
    """
    :param lst: An array of elements
    :return: The first element of the array
    """
    return lst[0]


def tail(lst):
    """
    :param lst: An array of elements
    :return: Every element besides the first one
    """
    if len(lst) == 1:
        return []
    else:
        return lst[1: len(lst) - 1]


# number 3
def r(lst):
    """ #3 (project)
    Translate the following functional pseudo-code for
    reversing a list into working code. The function should be
    named r. (Here + is list concatenation.) r([]) = []
    r(x :: xs) = r(xs) + [x]

    :param lst: An array of elements
    :return: The array of elements, but reversed in order
    """
    if lst == []:
        return []
    else:
        return r(tail(lst)).append(head(lst))


# number 4
def prod(m, n):
    """ #4 (project)
    Translate the following functional pseudo-code for
    multiplying natural numbers into working code. The function should
    be named prod. (HINT: The operator (')  is completely defined by the
    equations below. The definition is written using infix notation, but your
    implementation will not. It may help to start by rewriting the infix
    pseudo-code as prefix pseudo-code. For example, p(0, n) = 0, etc.)

    :param m: multiple
    :param n: number
    :return: the product of m * n
    """
    if m == 0:
        return 0
    else:
        return prod(m - 1, n) + n


# number 5
def fastPow(power, num):
    """
     (project) Translate the following functional pseudo-code for
      computing powers into working code. The base can be any type
      of number but the exponent must be a natural number. The function
      should be named fastPow.
      (HINT: The expressions 2k and 2k + 1
      indicate that the exponent is even or odd, respectively. Note that b^2
      does not involve a recursive call; it is just squaring.
      The definition is written using superscripts, but your implementation will not.
      It may help to start by rewriting this pseudo-code as prefix pseudo-code.
      For example, p(b, 0) = 1, etc.)

    :param power: The power the number is going to
    :param num: the chosen number, must be natural
    :return: number ^ power
    """
    if power == 0:
        return 1

    if power % 2 == 0:
        return fastPow(power - 2, num * num)
    else:
        return fastPow(power - 3, num * num) * num


# number 6
def prodAccum(m, n, a):
    """ #6 (project)
    Translate the following functional pseudo-code for
    multiplying natural numbers into working code.
    The function should be named prodAccum.
    prodAccum(0, n; a) = a
    prodAccum(m + 1, n; a) = prodAccum(m, n; n + a)

    :param m: multiple
    :param n: number
    :param a: accumulation
    :return: eventually the accumulation, but on a call when m != 0,
    it returns a  recursive call to m - 1, n, a + n
    """
    if m == 0:
        return a
    else:
        return prodAccum(m - 1, n, a + n)


def specialAdd(a, b):
    if a < 0 or b < 0:
        return -1
    else:
        return a + b


def specialMin(a, b):
    if a < 0:
        return b

    if b < 0:
        return a
    else:
        return min(a, b)


# number 7
def minChange(a, lst):
    if a == 0:
        return 0

    if a != 0 and lst == []:
        return 999  # number for failure

    if head(lst) > a:
        return minChange(a, tail(lst))
    else:
        return specialMin(specialAdd(1, minChange(a - head(list), tail(list))), minChange(a, tail(list)))

