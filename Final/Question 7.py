# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 13:20:22 2018

@author: mpkra
"""

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    timeStepRabbits = CURRENTRABBITPOP
    for rabbit in range(timeStepRabbits):
        if 1 - (CURRENTRABBITPOP/MAXRABBITPOP) > random.random():
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    timeStepFoxes = CURRENTFOXPOP
    for fox in range(timeStepFoxes):
        if CURRENTRABBITPOP > 10:
            if CURRENTRABBITPOP/MAXRABBITPOP > random.random():
                CURRENTRABBITPOP -= 1
                if random.random() < 1/3:
                    CURRENTFOXPOP += 1
            else:
                if CURRENTFOXPOP > 10 and random.random() < 9/10:
                    CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []
    for timeStep in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations

sim = runSimulation(200)
print(sim)
coeffRabbit = pylab.polyfit(range(200), sim[0], 2)
coeffFox = pylab.polyfit(range(200), sim[1], 2)

pylab.plot(pylab.arange(200), sim[0], label = 'RabbitPop')
pylab.plot(pylab.polyval(coeffRabbit, range(200)), 'k:', label = 'Regression Fit')
pylab.xlabel("Timesteps")
pylab.ylabel("Population")
pylab.title("Rabit Population")
pylab.legend(loc = 'best')
pylab.figure()

pylab.plot(pylab.arange(200), sim[1], 'r', label = 'FoxPop')
pylab.plot(pylab.polyval(coeffFox, range(200)), 'k:', label = 'Regression Fit')
pylab.xlabel("Timesteps")
pylab.ylabel("Population")
pylab.title("Fox Population")
pylab.legend(loc = 'best')



