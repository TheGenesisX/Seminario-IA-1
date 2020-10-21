class Sphere:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    
    def __init__(self):
        pass    #Nothing happens, but we need the constructor.
    
    def fitness(self, vector):
        z = 0
        
        for dimension in range(len(vector)):
            z += (vector[dimension]**2)
            
        return z