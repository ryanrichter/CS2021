# CS2021 Lab 02
# Required Questions

#  RQ1
from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = a - b
    else:
        f = a + b
    return f


#  RQ2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    if a > b and c > b:
        return (a*a) +(c*c)
    if a < b and c > b:
        return (b*b) + (c*c)
    if a > b and c < b:
        return (a*a) + (b*b)
    if a == b and b == c:
        return a*a + a*a


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n    

    # I have no idea why this 
    # series of loops fails the doctests.
    # When printing the exact 
    # tests that the doctest is running
    # the correct result is printed.
    # The doctest is registering the result
    # as "************" for some reason


         
#  RQ4
#  Write functions c, t, and f such that calling the with_if_statement and
#  calling the with_if_function do different things.
#  Such that the with_if_statement function returns the number 1, 
#  but calling the with_if_function function throws a ZeroDivisionError.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return 1
def t():
    return 1
def f():
    return 1

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)