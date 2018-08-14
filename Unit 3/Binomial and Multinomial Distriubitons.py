# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:49:16 2018

@author: mpkra
"""
import pylab

def factorial(n):
    total = n
    if n == 0:
        return 1
    while n > 1:
        total *= (n - 1)
        n -= 1
    return total

def ExactDiceSuccess(n, k, ranges):
    subsets = factorial(n)/(factorial(k)*factorial(n - k))
    success = (1/ranges)**k
    alternatives = ((ranges-1)/ranges)**(n-k)
    return subsets * success * alternatives
    
print(ExactDiceSuccess(10, 2, 6))

def plotProbSuccess(maxRolls, successes, ranges):
    rolls = []
    probs = []
    for i in range(successes, maxRolls):
        rolls.append(i)
        probs.append(ExactDiceSuccess(i, successes, ranges))
#    print(rolls, probs)
    pylab.plot(rolls, probs ) 
    pylab.xlabel('Rolls of Dice')
    pylab.ylabel('Probability of success')
    pylab.xlim(successes, maxRolls)
    pylab.ylim(0, 1.5*max(probs))
    pylab.title('Probability of exactly ' + str(successes) + \
                ' \nsuccesses rolling dice with '+ str(ranges) + ' sides')
print(plotProbSuccess(100, 3, 10))

