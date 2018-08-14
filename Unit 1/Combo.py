# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:03:47 2018

@author: mpkra
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            print(i, "shifted by", j, "is", i >> j)
            if (i >> j) % 2 == 1:
                print(i >> j, "divided by 2 has remainder 1", end=" ")
                print("so we'll append", items[j], "\n")
                combo.append(items[j])
        yield combo

test = ["fork", "knife", "spoon", "napkin"]

generateSet = powerSet(test)

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        combo = []
        combo1 = []
        for j in range(N):
            # test bit jth of integer i
            print(i, "operated on by", j, "is", i//3**j)
            if (i//3**j) % 3 == 2:
                print(i//3**j, "divided by 3 has remainder 2", end=" ")
                print("so we'll append", items[j], "\n")
                combo.append(items[j])
            elif (i//3**j) % 3 == 1:
                print(i//3**j, "divided by 3 has remainder 1", end=" ")
                print("so we'll append", items[j], "\n")
                combo1.append(items[j])
        yield (combo, combo1)

generateNewSet = yieldAllCombos(test)


def testAnotherSet(items):
    N = len(items)
    for i in range(2**N):
        bag = []
        for j in range(N):
            if (i // (2 ** j)) % 2 == 1:
                bag.append(items[j])
        yield bag