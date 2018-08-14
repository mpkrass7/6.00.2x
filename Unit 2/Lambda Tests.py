# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:23:26 2018

@author: mpkra
"""


orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]
minOrder = 100
total = list(map(lambda x: x if x[1] > minOrder else (x[0], x[1] + 10), 
                 map(lambda x : (x[0], x[2] * x[3]), orders)))
print(total)

test = (x**2 for x in range(10))
test2 = [x**2 for x in range(10)]
print(test.__next__())
print(test.__next__())
print(test.__next__())

print(list(test))
print(test2)

noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]

def notPrime():
    notPrimes = []
    for i in range(2, 8):
        for j in range(i * 2, 100, i):
            notPrimes.append(j)
    return notPrimes
print(noprimes)
print(notPrime())