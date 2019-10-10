# CS2021-Fall 2019 Required Questions 
# lab03.py

# RQ1
def doubletime(n):
    """Returns the result of doubling the number one n times
    >>> doubletime(0)
    1
    >>> doubletime(1)
    2
    >>> doubletime(10)
    1024
    """
    if (n == 0):
        return 1
    else:
        return 2*doubletime(n-1)

# RQ2
def skip2_add(n):
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.

    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    if (n <= 3):
        return n
    else:
        return n + skip2_add(n-3)



# RQ3
def a(n):
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)

    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    if (n == 0):
        return
    elif (n == 1):
        return 1
    elif (a(n-1) % 2 == 0):
        return int((3/2)*a(n-1))
    else:
        return int((3/2)*(a(n-1)+1))


#RQ4
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if (m == 1 or n == 1):
        return 1
    else:
        return paths(m-1,n) + paths(m,n-1)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)