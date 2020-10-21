import DE
import sphere
import rosenbrock
import quartic
import rastrigin
import drawer
import numpy as np

def main():
    sph = sphere.sphere()
    ros = rosenbrock.rosenbrock()
    qua = quartic.quartic()
    ras = rastrigin.rastrigin()
    draw = drawer.Drawer()
    
    aux = np.array([])
    graph = np.array([])
    executions = 5
    stepSize_parameter = 0.5    #[0.4, 0.9] (F in DE)
    crossover_rate = 0.7        #[0.1, 1.0] (c in DE)
    individuals = 30
    generations = 2000
    dimensions = 2
    
    graphName = "Sphere" + str(dimensions) + "D"
        
    for i in range(executions):
        aux = DE.differentialEvolution(sph, dimensions, individuals, stepSize_parameter, 
                                       crossover_rate, generations)
        
        if i == 0:      #For the first vector, we just make a copy to the one we'll be adding to.
            graph = aux
        else:           #For the rest, we just add.
            for a in range(len(aux)):
                graph[a] = graph[a] + aux[a]
                    
    for x in range(len(graph)):
        graph[x] = graph[x]/executions    #We obtain the average for each vector position.
            
    draw.drawIndividual(graph, graphName)
    
    file = open(graphName + ".txt", "w")
    for y in range(len(graph)):
        file.write(str(graph[y]) + "\n")
    file.close()
#    draw.drawGroup("Sphere") 
    
if __name__ == '__main__':
    main()