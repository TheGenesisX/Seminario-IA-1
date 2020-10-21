class sphere:
  MIN_VALUE = -5.12
  MAX_VALUE = 5.12
  
  def __init__(self):
      pass
  
  def fitness(self, vector):
      fit = 0.0
      for dimension in range(len(vector)):
          fit += vector[dimension]**2
      return fit