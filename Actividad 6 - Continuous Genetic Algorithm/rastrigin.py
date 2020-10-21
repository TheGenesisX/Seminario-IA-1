# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:19:58 2019

@author: qpqpq
"""
import math

class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    
    def __init__(self):
        pass
    
    def fitness(self, cromosoma):
        z = 0
        
        for i in range(len(cromosoma)):
            z += cromosoma[i]**2 - (10*math.cos(2*math.pi*cromosoma[i]))
            
        z += 10*(len(cromosoma))
        
        return z