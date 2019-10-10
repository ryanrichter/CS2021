def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    for number in range(0,n+1):
        print (number)

print (count_up(5))