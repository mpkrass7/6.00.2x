# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:31:07 2018

@author: mpkra
"""
import statistics
L = ['apples', 'oranges', 'kiwis', 'pineapples']
L1 = [10, 4, 12, 15, 20, 5]

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    lengths = []
    for i in L:
        lengths.append(len(i))
#    print(lengths)
#    easyStd = statistics.stdev(lengths)
    mean = sum(lengths)/len(lengths)
    total = 0.0
    for i in lengths:
        total += (mean - i)**2
    std = (total/len(L))**.5
    return std
    
print(stdDevOfLengths(L))

def stdNumbers(L):
    mean = sum(L)/len(L)
    total = 0.0
    for i in L:
        total += (i - mean)**2
    std = (total/len(L))**.5
    coefVar = std/mean
    return coefVar
print(stdNumbers(L1))