# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:52:25 2018

@author: mpkra
"""
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    def factorial(number):
        remaining = number
        total = number
        if number < 2:
            return 1
        while remaining > 1:
            remaining -= 1
            total *= remaining
        return total
    def allCombos(choices):
        options = len(choices)
        combinationTotal = 0
        for i in range(1, options + 1): #adds each set of combinations
            combinationTotal += factorial(options)/(factorial(i)\
                                          * (factorial(options - i)))
        return int(combinationTotal)
    
    combinations = []
    for i in range(allCombos(choices) + 1):
        ibin = bin(i)[2:]
        while len(ibin) < len(bin(allCombos(choices))[2:]):
            ibin = "0" + ibin
        combo = []
        for binary in ibin:
            combo.append(int(binary))
        combinations.append(combo)
    
    comboTotal = 0
    bestCombo = combinations[0]
    for combo in combinations:
        testCombo = []
        for index in range(len(combo)):
            testCombo.append(combo[index] * choices[index])
        if sum(testCombo) == total and sum(combo) < sum(bestCombo):
            comboTotal = total
            bestCombo = combo
        elif sum(testCombo) == total and comboTotal < total:
            comboTotal = total
            bestCombo = combo
        elif sum(testCombo) > comboTotal and sum(testCombo) <= total:
            comboTotal = sum(testCombo)
            bestCombo = combo
    return np.array(bestCombo)
    
print(find_combination([4, 6, 3, 5, 2], 10))

def factorial(number):
        remaining = number
        total = number
        if number < 2:
            return 1
        while remaining > 1:
            remaining -= 1
            total *= remaining
        return total
def allCombos(choices):
    options = len(choices)
    combinationTotal = 0
    for i in range(1, options + 1):
        combinationTotal += factorial(options)/(factorial(i)\
                                      * (factorial(options - i)))
    return int(combinationTotal)
    
#    for i in range(allCombos(choices) + 1):



#choices = [1, 2, 4, 5, 3]
#print(int(bin(allCombos(choices))[2:]))  
total = 4
