# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:13:36 2018

@author: mpkra
"""
import itertools

productList = ['ach', 'wire', 'card', 'pinacle', 'loc']

def prodPrimeCombos(prodList):
    
    def eratosthenes2(length, n = 1000):
        """returns a list of prime numbers of the length specified. If the 
        number is over 1000 (168 primes), user must define a higher n value!"""
        primeList = []
        multiples = set()
        for i in range(2, n+1):
            if i not in multiples:
                primeList.append(i)
                if len(primeList) == length:
                    return primeList
                multiples.update(range(i*i, n+1, i))
    
    primeList = eratosthenes2(len(prodList))
    
    def makeDict(products, values):
      """Make a dictinary of products from input list and prime numbers"""
        uniqueDict = {}
        for i in range(len(products)):
            uniqueDict[products[i]] = values[i]
        return uniqueDict
    
    valueDictionary = makeDict(prodList, primeList)
    
    def powerset(products):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        return itertools.chain.from_iterable(itertools.combinations(products, r) \
                                             for r in range(len(products)+1))
        
    productSets = list(powerset(prodList))
    
    def valueSets(productSets, valueDict):
        """Returns a list of tuples. First tuple value is a tuple of products
        Second tuple value is a unique value assigned to the combination"""
        groupValues = []
        for group in productSets:
            groupVal = 0
            for product in group:
                if groupVal == 0:
                    groupVal += valueDict[product]
                else:
                    groupVal *= valueDict[product]
            groupValues.append(groupVal)
        finalGroup = []
        for i in range(len(productSets)):
            finalGroup.append((productSets[i], groupValues[i]))
        return finalGroup
    
    return valueSets(productSets, valueDictionary)

print(prodPrimeCombos(productList))
#for counter, value in enumerate(productList, 2):
#print(counter, value)
