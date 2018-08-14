# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:54:34 2018

@author: mpkra
"""

import random
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)