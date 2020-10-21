class Knapsack:
    def __init__(self, valores):
        self._valores = valores

    def f(self, cromosoma):
        f = 0
        for i in range((len(cromosoma))-1):
            if cromosoma[i]:
                f = f + self._valores[i]
                if cromosoma[i+1] == 1:
                    f = f - self._valores[i]
                    f = f - self._valores[i+1]
        return f