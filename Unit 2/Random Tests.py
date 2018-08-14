# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:23:10 2018

@author: mpkra
"""

import random

def genEven():
    evenList = []
    for i in range(100):
        evenList.append(random.randrange(0, 100, 2))
    return evenList
print(genEven())

genEvens = (random.randrange(0, 100, 2) for x in range(100))
print(list(genEvens))

def nonRandom():
    random.seed(5324)
    return random.choice([10, 12, 14, 16, 18, 20])
print(nonRandom())
print(nonRandom())

dist1 = [random.random() * 2 - 1 for x in range(100)]
print(dist1)

print(random.random())