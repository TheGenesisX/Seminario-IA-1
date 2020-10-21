import math

class rastrigin:
  MIN_VALUE = -5.12
  MAX_VALUE = 5.12
  
  def __init__(self):
      pass
  
  def fitness(self, vector):
      fit = 0.0
      for dimension in range(len(vector)):
          fit += vector[dimension]**2 - (10*math.cos(2*math.pi*vector[dimension]))
      fit += 10*len(vector)
      return fit