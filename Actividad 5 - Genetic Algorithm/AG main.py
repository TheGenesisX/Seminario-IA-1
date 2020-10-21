import knapsack
import AG
#import queens

def main():
    pesos = [22, 14, 16, 23, 12, 15, 22, 6, 19, 20, 40, 8, 16, 6, 15, 21, 16]
    valores = [55, 34, 28, 30, 80, 3, 28, 24, 21, 43, 54, 12, 21, 11, 6, 21, 28]
    mochila = knapsack.Knapsack(pesos, valores, 100)
    #q = queens.Queens(4, 12)
    ag = AG.AG(18, 17, 1, 400, 0.1, mochila)
    #ag = AG.AG(32, 48, 4, 10000, 0.01, q)
    ag.run()

if __name__ == '__main__':
    main()
