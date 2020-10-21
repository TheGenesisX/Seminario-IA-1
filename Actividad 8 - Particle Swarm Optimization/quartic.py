class quartic:
    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    
    def __init__(self):
        pass
    
    def fitness(self, vector):
        fit = 0.0
        for dimension in range(len(vector)):
            fit += dimension*(vector[dimension]**4)
        return fit