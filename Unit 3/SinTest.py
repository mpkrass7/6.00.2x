# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 20:49:52 2018

@author: mpkra
"""

import math
import random
import numpy

def areaSin(numPoints):
    rectangle = math.pi
    inside = 0
    total = numPoints
    for i in range(numPoints):
        pointy = random.random()
        pointx = random.random() * rectangle
        if pointy <= math.sin(pointx):
            inside += 1
    mean = inside/total
    return mean

def multipleTrials(numTries, numPoints):
    means = []
    for i in range(numTries):
        means.append(areaSin(numPoints))
    Estimate = sum(means)/len(means) * math.pi
    stdDev = numpy.std(means)
    print('Est. = ' + str(Estimate) +\
          ', Std. dev. = ' + str(round(stdDev, 6))\
          + ', Needles = ' + str(numPoints))
    return(Estimate, stdDev)

def estSinInt(precision, numTries):
    points = 1000
    stdDev = precision
    while stdDev >= precision/2:
        estimate, stdDev = multipleTrials(numTries, points)
        points *= 2
    return estimate

estSinInt(.005, 100)