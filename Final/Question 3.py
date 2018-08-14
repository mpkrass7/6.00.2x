# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:00:22 2018

@author: mpkra
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    identicals = 0
    for trial in range(numTrials):
        numRed = 4
        numGreen = 4
        for i in range(3):
            if random.random() < numRed/(numRed + numGreen):
                numRed -= 1
            else:
                numGreen -= 1
        if (numRed == 1 or numGreen == 1):
            identicals += 1
    return identicals/numTrials

print(drawing_without_replacement_sim(100))