# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:33:38 2018

@author: mpkra
"""

import itertools

def powerset(items):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    #Make your iterable a list
    s = len(items)
    #First part chains the finished result together
    #Second part finds every combination of your list for length of r
    #Which ranges from 0 to the length of the list
    combonate = itertools.chain.from_iterable(itertools.combinations(items, r) for \
                                         r in range(s + 1))
    return list(combonate)
    
a = powerset([1,2,3])
print(a)
