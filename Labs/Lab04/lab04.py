##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    revList = lst[::-1]

    newList = lst + revList
    print(newList)


# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    first = []
    for x in seq:
        first += [fn(fn(x))]
    return first

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    x = []
    y = []
    for el in seq:
        if pred(el):
            x += [el]
        else:
            y += [el]
    return y

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    x = []
    for el in range(7):
        if pred(el):
            x += [el]
    return x

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    flatList = []

    for x in lst:
        if type(x) == list:
            flatList += flatten(x)
        else:
            flatList.append(x)
    return flatList


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)