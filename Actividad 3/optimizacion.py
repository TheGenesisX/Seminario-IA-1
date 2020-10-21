#######################Actividad 3. Optimizacion.#################################

import numpy as np
import matplotlib.pyplot as plt 

############################### EJERCICIO 1 ######################################

# y = 2x^3 - 6x^2 + 3x - 7
#
# 1) dy/dx = 6x^2 - 12x + 3
# 2)         6x^2 - 12x + 3 = 0
#
#Aplicamos formula general para resolver el problema.
#
# x = (12 +- sqrt(72))/12
# x = (12 +- 8.4852)/12
# 
# x1 = 1.7071
# x2 = 0.2929
#
# 3) Sustituir datos en la ecuacion original para encontrar y.
#
# Para x1 --> 2x^3 - 6x^2 + 3x -7
# y1 = -9.4142
#
# Para x2 --> 2x^3 - 6x^2 + 3x -7
# y2 = -6.5857
#
# Por lo tanto hay puntos estacionarios en:
#
# (1.7071, -9.4142)
# (0.2929, -6.5857)
#
# Clasificacion de los puntos estacionarios
#
# dy/dx = 6x^2 - 12x + 3
# d2y/d2x = 12x - 12
#
# Para x1 = 12x - 12 --> 12(1.7071) - 12 = 8.4852
# Por lo tanto tenemos un minimo en (1.7071, -9.4142)
#
# Para x2 = 12x - 12 --> 12(-0.2929) - 12 = -8.4852
# Por lo tanto tenemos un maximo en (0.2929, -6.5857)
# 
# Grafiquemos
###

#x = np.linspace(-1,3,130)
#y = (2*x**3) - (6*x**2) + (3*x) - 7
#
#min_max_x = [1.7071, 0.2929]
#min_max_y = [-9.4142, -6.5857]
#
#plt.text(min_max_x[0],min_max_y[0], 'Minimo: ' + '(' + str(min_max_x[0]) + ', ' 
#                                                    + str(min_max_y[0]) + ')')
#
#plt.text(min_max_x[1],min_max_y[1], 'Maximo: ' + '(' + str(min_max_x[1]) + ', '
#                                                     + str(min_max_y[1]) + ')')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('2x^3 - 6x^2 + 3x - 7')
#plt.plot(min_max_x,min_max_y,'*r')
#plt.plot(x,y,'b')
#plt.show()

##################################################################################

############################## EJERCICIO 2 #######################################

# y = 3x^3 - 5x^2 + 2x
#
# 1) dy/dx = 9x^2 - 10x + 2
# 2)         9x^2 - 10x + 2 = 0
#
#Aplicamos formula general para resolver el problema.
#
# x = (10 +- sqrt(28))/18
# x = (10 +- 5.2915)/18
# 
# x1 = 0.8495
# x2 = 0.2615
#
# 3) Sustituir datos en la ecuacion original para encontrar y.
#
# Para x1 --> 3x^3 - 5x^2 + 2x
# y1 = -0.0701
#
# Para x2 --> 3x^3 - 5x^2 + 2x
# y2 = 0.2347
#
# Por lo tanto hay puntos estacionarios en:
#
# (0.8495, -0.0701)
# (0.2615, 0.2347)
#
# Clasificacion de los puntos estacionarios
#
# dy/dx = 9x^2 - 10x + 2
# d2y/d2x = 18x - 10
#
# Para x1 = 18x - 10 --> 18(0.8495) - 10 = 5.291
# Por lo tanto tenemos un minimo en (0.8495, -0.0701)
#
# Para x2 = 18x = 10 --> 18(0.2615) - 10 = -5.293
# Por lo tanto tenemos un maximo en (0.2615, 0.2347)
# 
# Grafiquemos
###

#x = np.linspace(-1,3,130)
#y = (3*x**3) - (5*x**2) + (2*x)
#
#min_max_x = [0.8495, 0.2615]
#min_max_y = [-0.0701, 0.2347]
#
#plt.text(min_max_x[0],min_max_y[0], 'Minimo: ' + '(' + str(min_max_x[0]) + ', ' 
#                                                     + str(min_max_y[0]) + ')')
#
#plt.text(min_max_x[1],min_max_y[1], 'Maximo: ' + '(' + str(min_max_x[1]) + ', '
#                                                     + str(min_max_y[1]) + ')')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('3x^3 - 5x^2 + 2x')
#plt.plot(min_max_x,min_max_y,'*r')
#plt.plot(x,y,'b')
#plt.show()

##################################################################################

############################## EJERCICIO 3 #######################################

# y = 4x^3 + 9x^2 - 3x - 6
#
# 1) dy/dx = 12x^2 + 18x - 3
# 2)         12x^2 + 18x - 3 = 0
#
#Aplicamos formula general para resolver el problema.
#
# x = (-18 +- sqrt(468))/24
# x = (-18 +- 21.6333)/24
# 
# x1 = 0.1513
# x2 = -1.6513
#
# 3) Sustituir datos en la ecuacion original para encontrar y.
#
# Para x1 --> 4x^3 + 9x^2 - 3x - 6
# y1 = -6.2340
#
# Para x2 --> 4x^3 + 9x^2 - 3x - 6
# y2 = 5.4840
#
# Por lo tanto hay puntos estacionarios en:
#
# (0.1513, -6.2340)
# (-1.6513, 5.4840)
#
# Clasificacion de los puntos estacionarios
#
# dy/dx = 12x^2 + 18x - 3
# d2y/d2x = 24x + 18
#
# Para x1 = 24x + 18 --> 24(0.1513) + 18 = 3.6312
# Por lo tanto tenemos un minimo en (0.1513, -6.2340)
#
# Para x2 = 24x + 18 --> 24(-1.6513) + 18 = -21.6313
# Por lo tanto tenemos un maximo en (-1.6513, 5.4840)
# 
# Grafiquemos
###

#x = np.linspace(-4,3,130)
#y = (4*x**3) + (9*x**2) - (3*x) - 6
#
#min_max_x = [0.1513, -1.6513]
#min_max_y = [-6.2340, 5.4840]
#
#plt.text(min_max_x[0],min_max_y[0], 'Minimo: ' + '(' + str(min_max_x[0]) + ', ' 
#                                                     + str(min_max_y[0]) + ')')
#
#plt.text(min_max_x[1],min_max_y[1], 'Maximo: ' + '(' + str(min_max_x[1]) + ', '
#                                                     + str(min_max_y[1]) + ')')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('4x^3 + 9x^2 - 3x - 6')
#plt.plot(min_max_x,min_max_y,'*r')
#plt.plot(x,y,'b')
#plt.show()

##################################################################################

############################## EJERCICIO 4 #######################################

# y = 2x^3 + 5x^2 + 3x
#
# 1) dy/dx = 6x^2 + 10x + 3
# 2)         6x^2 + 10x + 3 = 0
#
#Aplicamos formula general para resolver el problema.
#
# x = (-10 +- sqrt(28))/12
# x = (-10 +- 5.2915)/12
# 
# x1 = -0.3923
# x2 = -1.2742
#
# 3) Sustituir datos en la ecuacion original para encontrar y.
#
# Para x1 --> 2x^3 + 5x^2 + 3x
# y1 = -0.5281
#
# Para x2 --> 2x^3 + 5x^2 + 3x
# y2 = 0.1577
#
# Por lo tanto hay puntos estacionarios en:
#
# (-0.3923, -0.5281)
# (-1.2742, 0.1577)
#
# Clasificacion de los puntos estacionarios
#
# dy/dx = 6x^2 + 10x + 3
# d2y/d2x = 12x + 10
#
# Para x1 = 12x + 10 --> 12(-0.3923) + 10 = 5.2924
# Por lo tanto tenemos un minimo en (-0.3923, -0.5281)
#
# Para x2 = 12x + 10 --> 12(-1.2742) + 10 = -5.2904
# Por lo tanto tenemos un maximo en (-1.2742, 0.1577)
# 
# Grafiquemos
###

x = np.linspace(-4,3,130)
y = (2*x**3) + (5*x**2) + (3*x)

min_max_x = [-0.3923, -1.2742]
min_max_y = [-0.5281, 0.1577]

plt.text(min_max_x[0],min_max_y[0], 'Minimo: ' + '(' + str(min_max_x[0]) + ', ' 
                                                     + str(min_max_y[0]) + ')')

plt.text(min_max_x[1],min_max_y[1], 'Maximo: ' + '(' + str(min_max_x[1]) + ', '
                                                     + str(min_max_y[1]) + ')')

plt.xlabel('x')
plt.ylabel('y')
plt.title('2x^3 + 5x^2 + 3x')
plt.plot(min_max_x,min_max_y,'*r')
plt.plot(x,y,'b')
plt.show()

##################################################################################

######################## EJERCICIO DE EJEMPLO EN CLASE############################

#x = np.linspace(-1,3,128)
##Generamos 130 puntos de grafico desde -1 hasta 3.
#
#y = x**3 - (4*x**2) + x + 6
##Nuestra funcion original.
#
#min_max_x = [2.53,0.13]
##vector para las coordenadas en X
#
#min_max_y = [-0.88,6.09]
##Vector para las coordenadas en Y
#
#plt.text(min_max_x[0],min_max_y[0], 'Minimo: ' + '(' + str(min_max_x[0]) + ', ' 
#                                                     + str(min_max_y[0]) + ')')
#
#plt.text(min_max_x[1],min_max_y[1], 'Maximo: ' + '(' + str(min_max_x[1]) + ', '
#                                                     + str(min_max_y[1]) + ')')
##Ponemos etiquetas de "Minimo" y "Maximo" en los puntos correspondientes de la grafica.
#
#plt.xlabel('x')
#plt.ylabel('y')
##Hacemos que se vean las letras X y Y en sus correspondientes ejes.
#
#plt.title('x^3 - 4x^2 + x + 6')
##Agregamos como titulo nuestra funcion.
#
#plt.plot(min_max_x,min_max_y,'*r')
##Imprimimos en la grafica como asteriscos rojos los puntos minimo y maximo.
#
#plt.plot(x,y,'b')
#
#plt.show()