from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm    #Para modelos de color
import numpy as np

#############################EJERCICIO 1##############################################
#fig = plt.figure()
#ax = fig.gca(projection = '3d')
#
#x = np.arange(-5.12,5.12,0.01) #Puntos de -5.12 hasta 5.12 con aumentos de 0.01 en eje X.
#y = np.arange(-5.12,5.12,0.01) #Puntos de -5.12 hasta 5.12 con aumentos de 0.01 en eje Y.
#x,y = np.meshgrid(x,y)
#z = x**2 + y**2    #Nuestra funcion generada en terminos de Z.
#
#surf = ax.plot_surface(x, y, z, cmap = cm.coolwarm)
#fig.colorbar(surf)
#fig.show()
##############################################################

#########################EJERCICIO 2#################################################
#fig = plt.figure()
#ax = fig.gca(projection = '3d')
#
#x = np.arange(-2.048,2.048,0.01) #Puntos de -2.048 hasta 2.048 con aumentos de 0.01 en eje X.
#y = np.arange(-2.048,2.048,0.01) #Puntos de -2.048 hasta 2.048 con aumentos de 0.01 en eje Y.
#x,y = np.meshgrid(x,y)
#z = 100*(y - (x**2))**2 + (x - 1)**2  #Nuestra funcion generada en terminos de Z.
#
#surf = ax.plot_surface(x, y, z, cmap = cm.coolwarm)
#fig.colorbar(surf)
#fig.show()
##############################################################

#########################EJERCICIO 3#################################################
#fig = plt.figure()
#ax = fig.gca(projection = '3d')
#
#x = np.arange(-5.12,5.12,0.01) #Puntos de -5.12 hasta 5.12 con aumentos de 0.01 en eje X.
#y = np.arange(-5.12,5.12,0.01) #Puntos de -5.12 hasta 5.12 con aumentos de 0.01 en eje Y.
#x,y = np.meshgrid(x,y)
#z = 10*2 + (x**2 - 10*(np.cos(2*np.pi*x))) + (y**2 - 10*(np.cos(2*np.pi*y)))     
##Nuestra funcion generada en terminos de Z.
#
#surf = ax.plot_surface(x, y, z, cmap = cm.coolwarm)
#fig.colorbar(surf)
#fig.show()
#############################################################

#########################EJERCICIO 4#################################################
fig = plt.figure()
ax = fig.gca(projection = '3d')

x = np.arange(-1.28,1.28,0.01) #Puntos de -1.28 hasta 1.28 con aumentos de 0.01 en eje X.
y = np.arange(-1.28,1.28,0.01) #Puntos de -1.28 hasta 1.28 con aumentos de 0.01 en eje Y.
x,y = np.meshgrid(x,y)
z = 1*(x**4) + 2*(y**4)

surf = ax.plot_surface(x, y, z, cmap = cm.coolwarm)
fig.colorbar(surf)
fig.show()
##############################################################