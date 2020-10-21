import matplotlib.pyplot as plt
import numpy as np

class Drawer:
    
    def __init__(self):
        pass
    
    def drawIndividual(self, array, title):
        plt.plot(array, 'ro', array, 'b')
        plt.axis([0,20,0,1000]) #xmin, xmax, ymin, ymax
        plt.ylabel('Evaluaciones')
        plt.xlabel('Generaciones')
        plt.title(title)
        plt.savefig(title + '.png', dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format='png',
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None, metadata=None)
        plt.show()
        
    def drawGroup(self, title):
        a1 = a2 = a3 = a4 = np.array([])
        dimensionsArray = np.array([2,4,8,16])
        
        for i in range(4):
            file = open(title + str(dimensionsArray[i]) + "D" + ".txt", "r")
            data = file.read().splitlines()
            file.close()
            aux = np.array([])
            for a in range(len(data)):
                num = float(data[a])
                aux = np.append(aux, [num])
            if i == 0:
                a1 = aux
            if i == 1:
                a2 = aux
            if i == 2:
                a3 = aux
            if i == 3:
                a4 = aux
            
        plt.plot(a1, 'ro', a1, 'b',
                 a2, 'ro', a2, 'b',
                 a3, 'ro', a3, 'b',
                 a4, 'ro', a4, 'b')
        plt.axis([0,20,0,1000])
        plt.ylabel('Evaluaciones')
        plt.xlabel('Generaciones')
        plt.title(title)
        plt.savefig(title + '.png', dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format='png',
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)
        plt.show()