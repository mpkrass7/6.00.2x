# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:50:48 2018

@author: mpkra
"""

class test(object):
    def __init__(self, where, when):
        self.place = where
        self.time = when
    
class innerTest(test):
    def showWhereWhen():
        print(where, when)
        
    