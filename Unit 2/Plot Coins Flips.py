# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 07:53:12 2018

@author: mpkra
"""
import pylab
import random

def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp +1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    print("xAxis:", xAxis, "ratios:", ratios, "diffs:", diffs)
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of FLips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis, diffs, 'ko')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis, ratios, 'ko')
random.seed(0)
flipPlot(4, 20)