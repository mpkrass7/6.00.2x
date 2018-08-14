# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 09:59:38 2018

@author: mpkra
"""
list1 =  [3, 4, -1, 5, -4]
list2 = [3, 4, -8, 15, -1, 2]

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    lists = []
    def intermediary(L):
        if len(L) == 1:
            lists.append(L)
            return
        elif L in lists:
            pass
        else:  
            lists.append(L)
            intermediary(L[0:len(L)-1])
            intermediary(L[1:len(L)])
            return
    lists.append(intermediary(L))
    lists = lists[:-1]
    maxSum = 0
    maxList = []
    for i in lists:
        if sum(i) > maxSum:
            maxList = i
            maxSum = sum(i)
    return maxSum

print("x")
print(max_contig_sum(list2))
