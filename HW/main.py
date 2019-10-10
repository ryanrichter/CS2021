"""
Egyptian Functions by Ryan Richter
CS2021
9/27/19

"""

import math

def egypt(n,d):
    """
    >>> egypt(3,4)
    1/2 + 1/4
    >>> egypt(11,12)
    1/2 + 1/3 + 1/12 
    >>> egypt(123,124)
    1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112
    """

    result = [] " A list to both hold the results of the operations but also to keep track of how many functions will need to be output "

    while (n != 0):
        x = math.ceil(d/n) " Dividing the demoninator by the numerator and rounding up "
        result.append(x) " Appending the result to the 'result' list "

        n = x * n - d " Setting new numerator and denominator "
        d = d * x

    for i in range(len(result)): " For the amount of times the above loop was run "
        if (i != len(result)-1): " If the current fraction is not the last one "
            print("1/{0} +" .    " Print it "
                    format(result[i]), end = " ") 
        else:                    " If the current fraction is the last one "
            print("1/{0}" .      " Print it without a plus sign "
                    format (result[i]), end = " ")

n = input('p? ') " Input numerator and denominator "
d = input('q? ')

n = float(n)     " Changing from string to float "
d = float(d)

egypt(n,d)       " Calling the function "

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
" These doctests don't seem to want to work. I have the exact same output but it is marking the tests as failed."