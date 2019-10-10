__author__ = "Ryan Richter" # Your name
__email__ = "richterw@mail.uc.edu" # Your email address
"""Four Required questions for Lab 1"""
 
## Boolean Operators ##
# RQ1
def both_negative(x, y):
    """Returns True if and only if both x and y are negative.
 
    >>> both_negative(-1, 1)
    False
    >>> both_negative(1, 2)
    False
    >>> both_negative(-1, -2)
    True
    """
    if (x<0) & (y<0):
      return True
    else:
      return False
    
 
 
## while Loops ##
# RQ2
def not_factor (n):
    """Prints out all of the numbers less than n which do not divide `n` evenly.
 
    >>> not_factor(10)
    9
    8
    7
    6
    4
    3
    """
    i = n
    while i > 0:
      if n % i != 0:
        print(i)
    i-=1
    
    
      

      


 
# RQ3
def lucas(n):
    """Returns the nth Lucas number.
      Lucas numbers form a series similar in pattern to the Fibonacci sequence:
      2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,...
 
    >>> lucas(0)
    2
    >>> lucas(1)
    1
    >>> lucas(2)
    3
    >>> lucas(3)
    4
    >>> lucas(11)
    199
    >>> lucas(100)
    792070839848372253127
    """
    if (n==0):
      return 2
    if (n==1):
      return 1
    return lucas(n-1) + lucas(n-2)

#RQ4
def gets_discount(p1, p2, p3):
    """ Returns True if p1 is an adult (age at least 18) and p2 and p3 are both children (age 12 or below), 
    False otherwise. Do not use if statement.
    >>> gets_discount(15, 12, 11)
    False
    >>> gets_discount(90, 7, 12)
    True
    >>> gets_discount(18, 18, 18)
    False
    >>> gets_discount(40, 7, 15)
    False
    """
    return (p1 >= 18 and p2 <= 12 and p3 <= 12) or (p1 < 18 and p2 > 12 and p3 > 12)
    


 
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
