import numpy as np
import matplotlib.pyplot as plt

class Graphic:
    
    def __init(self, direccion):
        self._direccion = direccion
    
    def leer(self, direccion):  #Lee un txt con los datos de los mejores historicos, los transforma a floats (porque se leen como str)
        array = np.array([])    #los agrega a un array, y lo retorna
        
        archivo = open(direccion, "r")
        datos = archivo.read().splitlines()
        archivo.close()
        
        for i in range(len(datos)):
            num = float(datos[i])
            array = np.append(array, [num])

        return array       

    def graficar(self, array1, array2, array3, array4, array5, y_limit, title):    #y_limit son los puntos a graficar en el eje Y.
        array_Y = np.array([])
        
        for i in range(20):
            Y = 0
            Y += array1[i]
            Y += array2[i]
            Y += array3[i]
            Y += array4[i]
            Y += array5[i]
            Y /= 5
            
            array_Y = np.append(array_Y, [Y])
        
        plt.plot(array_Y, 'ro', array_Y, 'b')
        plt.axis([0,20,0,y_limit])
        plt.ylabel('Evaluaciones')
        plt.xlabel('Generaciones')
        plt.title(title)
        plt.show()
        return array_Y
    
    def mesh(self, g1, g2, g3, g4, y_limit, title):
        plt.plot(g1, 'ro', g1, 'b', g2, 'ro', g2, 'b', g3, 'ro', g3, 'b', g4, 'ro', g4, 'b')
        plt.axis([0,20,0,y_limit])
        plt.ylabel('Evaluaciones')
        plt.xlabel('Generaciones')
        plt.title(title)
        plt.show()