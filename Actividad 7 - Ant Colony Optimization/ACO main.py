import rosenbrock
import sphere
import rastrigin
import quartic
import ACO
import drawer
import numpy as np

def main():    
    ros = rosenbrock.Rosenbrock()
    sph = sphere.Sphere()
    qua = quartic.Quartic()
    ras = rastrigin.Rastrigin()
    
    aux = np.array([])
    graph = np.array([])
    ejecuciones = 1
    draw = drawer.Drawer()
    
    
    individuos = 32
    dimensiones = 16
    intervalos = 8
    a = 1
    Q = 20
    evaporacion = 0.9
    t0 = 0.00001
    generaciones = 100
    bestFitnessPos = 100
    
    
    graphName = "Quartic" + str(dimensiones) + "D"
    aco = ACO.ACO(individuos, 
                  dimensiones, 
                  intervalos, 
                  a, 
                  Q,
                  evaporacion,
                  t0,
                  ras,
                  generaciones,
                  bestFitnessPos)
        
    for i in range(ejecuciones):
        aux = aco.run()
        if i == 0:
            graph = aux
        else:           #Sumamos el resto de las ejecuciones.
            for a in range(len(aux)):
                graph[a] = graph[a] + aux[a]
                    
    for x in range(len(graph)):
        graph[x] = graph[x]/ejecuciones    #Obtenemos el promedio de cada posicion
            
    draw.drawIndividual(graph, graphName)
    
    file = open(graphName + ".txt", "w")
    for y in range(len(graph)):
        file.write(str(graph[y]) + "\n")
    file.close()
    #draw.drawGroup("Quartic")
        
    
    
if __name__ == '__main__':
    main()
