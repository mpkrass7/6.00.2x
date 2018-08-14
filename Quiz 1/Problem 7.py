# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 11:21:06 2018

@author: mpkra
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    i = 0
    while True:
        if test(i):
            return i
        elif test(-i):
            return -i
        else:
            i += 1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

def f(x):
    return [1,2,3][-x] == 1 and x != 0
print(solveit(f))