# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:31:00 2019

@author: Usuario
"""

class Sphere:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for alelo in cromosoma:
            z += alelo**2
        return z