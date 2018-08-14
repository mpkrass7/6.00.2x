# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:20:52 2018

@author: mpkra
"""

import random
import numpy

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    
    def runTrial():
        options = ['r', 'r', 'r', 'g', 'g', 'g']
        picks = []
        success = 0
        for i in range(3):
            pick = random.choice(options)
            picks.append(pick)
            options.remove(pick)
        if picks[0] == picks[1] == picks[2]:
            success += 1
        return success
    trialResults = []
    for i in range(numTrials):
        trialResults.append(runTrial())
    successEstimate = sum(trialResults)/len(trialResults)
#    stdDev = numpy.std(trialResults)
    return successEstimate
    

print(noReplacementSimulation(5))
print(noReplacementSimulation(50))
print(noReplacementSimulation(500))
print(noReplacementSimulation(5000))
print(noReplacementSimulation(50000))
print(noReplacementSimulation(500000))

