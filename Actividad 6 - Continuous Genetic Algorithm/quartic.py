# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:10:54 2019

@author: qpqpq
"""

class Quartic:
    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    
    def __init__(self):
        pass
    
    def fitness(self, cromosoma):
        z = 0

        for i in range(len(cromosoma)):
            z += i * (cromosoma[i]**4)
            
        return z