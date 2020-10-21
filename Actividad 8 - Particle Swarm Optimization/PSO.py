import random
import copy
import sys
import numpy as np

class Particle:
  def __init__(self, dimensions, ecuation, seed):
    #Inicializamos en cero los vectores de los individuos.
    self.rnd = random.Random(seed)
    self.position = [0.0 for i in range(dimensions)]   #Posicion de la particula, correspondiente a cada dimension.
    self.velocity = [0.0 for i in range(dimensions)]   #Velocidad de la particula, correspondiente a cada dimensaion.
    self.best_part_pos = [0.0 for i in range(dimensions)]  #Mejor posicion individual de la particula en cada iteracion.

    #Le damos un valor aleatorio a cada posicion de velocidad y localizacion de la particula.
    for i in range(dimensions):
      self.position[i] = ((ecuation.MAX_VALUE - ecuation.MIN_VALUE) * self.rnd.random() + ecuation.MIN_VALUE)
      self.velocity[i] = ((ecuation.MAX_VALUE - ecuation.MIN_VALUE) * self.rnd.random() + ecuation.MIN_VALUE)

    #self.fitness = fitness(self.position) #Fitness actual.
    self.fitness = ecuation.fitness(self.position)
    self.best_part_pos = copy.copy(self.position) 
    self.best_part_err = self.fitness #Mejor fitness actual.
    
    
def PSOrun(max_iterations, n, dimensions, ecuation, weight, C_L, S_L):
  rnd = random.Random(0)
  swarm = [Particle(dimensions, ecuation, i) for i in range(n)]   #Crea tantas particulas como le indiquemos.

  best_swarm_pos = [0.0 for i in range(dimensions)]
  best_swarm_fitness = sys.float_info.max #Mejor fitness del enjambre.
  for i in range(n): #Para cada particula.
    if swarm[i].fitness < best_swarm_fitness:   #Si el fitness de una particula es mejor que el global, actualizamos.
      best_swarm_fitness = swarm[i].fitness
      best_swarm_pos = copy.copy(swarm[i].position) 

  iterations = 0
  w = weight    #Inercia de la velocidad.
  c1 = C_L #Proporcion de aprendizaje cognitivo.
  c2 = S_L #Proporcion de aprendizaje social.
  
  graphData = 0   #El dato que obtenemos de cada 100 generaciones
  graphArray = np.array([])    #Array donde almacenamos cada graphData

  while iterations < max_iterations:
    if iterations % 100 == 0:
        graphData = best_swarm_fitness
        graphArray = np.append(graphArray, [graphData])      
        
    print("Iteration: ", iterations, " ", best_swarm_pos, best_swarm_fitness)
      
    for i in range(n): #Procesamos cada particula
      for k in range(dimensions): 
        r1 = rnd.random()    
        r2 = rnd.random()
    
        #Actualizamos la velocidad de la particula.
        swarm[i].velocity[k] = ((w * swarm[i].velocity[k]) + (c1 * r1 * (swarm[i].best_part_pos[k] -
          swarm[i].position[k])) + (c2 * r2 * (best_swarm_pos[k] - swarm[i].position[k])))  

        #Nos aseguramos de que las particulas no se salgan del dominio de busqueda de la solucion.
        if swarm[i].velocity[k] < ecuation.MIN_VALUE:
          swarm[i].velocity[k] = ecuation.MIN_VALUE
        elif swarm[i].velocity[k] > ecuation.MAX_VALUE:
          swarm[i].velocity[k] = ecuation.MAX_VALUE
        #Para cualquier limite (positivo o negativo) que rebasen, lo corregimos.

      #Actualizamos la posición de acuerdo a la velicidad.
      for k in range(dimensions): 
        swarm[i].position[k] += swarm[i].velocity[k]
  
      #Calculamos el fitness de la nueva posicion.
      swarm[i].fitness = ecuation.fitness(swarm[i].position)

      #Verificamos si la nueva posicion es un nuevo mejor para la particula.
      if swarm[i].fitness < swarm[i].best_part_err:
        swarm[i].best_part_err = swarm[i].fitness
        swarm[i].best_part_pos = copy.copy(swarm[i].position)

      #Verificamos si la nueva posicion es un mejor global.
      if swarm[i].fitness < best_swarm_fitness:
        best_swarm_fitness = swarm[i].fitness
        best_swarm_pos = copy.copy(swarm[i].position)
    
    iterations += 1
  return graphArray