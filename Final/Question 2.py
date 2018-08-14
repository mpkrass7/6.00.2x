# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:38:19 2018

@author: mpkra
"""

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
pylab.hist(xVals)
pylab.figure()
pylab.hist(tVals)
test= []
for i in range(1000):
    test.append(i)
pylab.figure()

pylab.plot(xVals, yVals)