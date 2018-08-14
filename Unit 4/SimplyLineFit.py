# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:45:04 2018

@author: mpkra
"""
import pylab
import numpy as np

x = [2, 7, 3, 7, 4, 5, 10]
y = [4, 8, 12, 23, 16, 15, 30]
def bestFit(x, y):
    assert len(x) == len(y), "Not the same lengths"
    slope = .1
    intercept = 0
    lowResult = 0
    bestIntercept = intercept
    bestSlope = slope
    cycleCount = 0
    while intercept < max(y):
        while slope < max(y) - min(y):
            results = []
            for i in range(len(x)):
                resultDiff = (((x[i] * slope) + intercept) - y[i])**2
                results.append(resultDiff)
            sumSquares = round(sum(results),1)
#            print("sum squares for slope:", round(slope, 1), \
#                  "intercept:", round(intercept, 1), "=", sumSquares)
            if lowResult == 0 or sumSquares < lowResult:
                lowResult = sumSquares
                bestSlope = slope
                bestIntercept = intercept
#                print("sum squares for slope:", round(slope, 1), \
#                  "intercept:", round(intercept, 1), "=", sumSquares)
            cycleCount += 1
            slope = round(slope + .1, 1)
        intercept = round(intercept + .1, 1)
        slope = .1
    pylab.plot(x, y, 'bo', label = "Actual Values")
    pylab.xlabel("Independent Variable")
    pylab.ylabel("Dependent Variable")
    pylab.title("Find Best Fit")
    estValues = bestSlope * pylab.array(x) + bestIntercept
    pylab.plot(x, estValues, 'k:', label = "Fit Values")
    print(lowResult)
    return estValues 

estimations = bestFit(x, y)


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    meanY = sum(y)/len(y)
    arrayY = np.array(y)
    arrayEst = np.array(estimated)
    SSE = ((arrayY - arrayEst)**2).sum()
    MV = ((arrayY - meanY)**2).sum()
    return 1 - (SSE/MV)

print(r_squared(y, estimations))