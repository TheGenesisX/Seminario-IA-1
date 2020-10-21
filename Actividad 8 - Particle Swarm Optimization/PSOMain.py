import PSO
import rastrigin
import quartic
import sphere
import rosenbrock
import drawer
import numpy as np

def main():
#    ras = rastrigin.rastrigin()
#    qua = quartic.quartic()
#    sph = sphere.sphere()
#    ros = rosenbrock.rosenbrock()
#    
#    aux = np.array([])
#    graph = np.array([])
#    ejecuciones = 5
     draw = drawer.Drawer()
#    
#    dimensions = 16
#    num_particles = 50
#    max_iterations = 2000    #Generaciones
#    weight = 0.729    #Inercia de la velocidad.
#    cognitive_learning = 1.49445 #Proporcion de aprendizaje cognitivo.
#    social_learning = 1.49445 #Proporcion de aprendizaje social.
#    
#    graphName = "Quartic" + str(dimensions) + "D"
#        
#    for i in range(ejecuciones):
#        aux = PSO.PSOrun(max_iterations, num_particles, dimensions, qua, weight, 
#                         cognitive_learning, social_learning)
#        if i == 0:
#            graph = aux
#        else:           #Sumamos el resto de las ejecuciones.
#            for a in range(len(aux)):
#                graph[a] = graph[a] + aux[a]
#                    
#    for x in range(len(graph)):
#        graph[x] = graph[x]/ejecuciones    #Obtenemos el promedio de cada posicion
#            
#    draw.drawIndividual(graph, graphName)
#    
#    file = open(graphName + ".txt", "w")
#    for y in range(len(graph)):
#        file.write(str(graph[y]) + "\n")
#    file.close()
     draw.drawGroup("Quartic")    
    
if __name__ == '__main__':
    main()