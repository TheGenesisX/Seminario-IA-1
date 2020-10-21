# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:30:22 2019

@author: Usuario
"""

#import sphere
#import rosenbrock
#import quartic
#import rastrigin
#import AGC
import graphic
import numpy as np

def main():
    #sp = sphere.Sphere()
    #ro = rosenbrock.Rosenbrock()
    #ra = rastrigin.Rastrigin()
    #qu = quartic.Quartic()
    
    #ag = AGC.AGC(32, 16, 2000, 0.02, sp)
    #ag = AGC.AGC(32, 16, 2000, 0.02, ro)
    #ag = AGC.AGC(32, 16, 2000, 0.02, ra)
    #ag = AGC.AGC(32, 16, 2000, 0.02, qu)
    
    #ag.run()
    
###############################################################################
    
    a1 = a2 = a3 = a4 = a5 = np.array([])
    b1 = b2 = b3 = b4 = np.array([])
    
    g = graphic.Graphic()
    
    a1 = g.leer("quartic2_1.txt")
    a2 = g.leer("quartic2_2.txt")
    a3 = g.leer("quartic2_3.txt")
    a4 = g.leer("quartic2_4.txt")
    a5 = g.leer("quartic2_5.txt")
    b1 = g.graficar(a1, a2, a3, a4, a5, 0.2, 'Quartic 2D')  
    
    a1 = g.leer("quartic4_1.txt")
    a2 = g.leer("quartic4_2.txt")
    a3 = g.leer("quartic4_3.txt")
    a4 = g.leer("quartic4_4.txt")
    a5 = g.leer("quartic4_5.txt")
    b2 = g.graficar(a1, a2, a3, a4, a5, 0.2, 'Quartic 4D') 
    
    a1 = g.leer("quartic8_1.txt")
    a2 = g.leer("quartic8_2.txt")
    a3 = g.leer("quartic8_3.txt")
    a4 = g.leer("quartic8_4.txt")
    a5 = g.leer("quartic8_5.txt")
    b3 = g.graficar(a1, a2, a3, a4, a5, 2.5, 'Quartic 8D') 
    
    a1 = g.leer("quartic16_1.txt")
    a2 = g.leer("quartic16_2.txt")
    a3 = g.leer("quartic16_3.txt")
    a4 = g.leer("quartic16_4.txt")
    a5 = g.leer("quartic16_5.txt")
    b4 = g.graficar(a1, a2, a3, a4, a5, 19, 'Quartic 16D') 
    
    g.mesh(b1, b2, b3, b4, 19, 'Quartic')
    
    

if __name__ == '__main__':
    main()