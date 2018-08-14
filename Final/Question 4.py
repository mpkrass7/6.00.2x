# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:10:14 2018

@author: mpkra
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()
    

#makeHistogram([1,2,3,4,5,6,6,6,7], 7, "DiceRoll", "Frequency", "test")
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    
    def findMaxRun(die, numRolls):
        maxRun, localMax = 1, 1 
        rolls = []
        for roll in range(numRolls):
            if roll == 0:
                rolls.append(die.roll())
            else:
                rolls.append(die.roll())
                if rolls[-1] == rolls[-2]:
                    localMax += 1
                elif localMax > maxRun:
                    maxRun = localMax
                    localMax = 1
#                    print("New max:", maxRun, "on", rolls[-2])
                else:
                    localMax = 1
            if localMax > maxRun:
                maxRun = localMax
        return maxRun
    maxRuns = []
    for trial in range(numTrials):
        maxRuns.append(findMaxRun(die, numRolls))
    makeHistogram(maxRuns, 10, "Longest Run", "Run Frequency",\
                  "Impact of this dice")
    return(sum(maxRuns)/len(maxRuns))
    # TODO
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))