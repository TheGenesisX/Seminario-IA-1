import random
import numpy as np

#We make sure that the individual won't go out of the ecuation solution bounds.
def ensure_bounds(vector, ecuation):
    new_vector = []
    
    for i in range(len(vector)):
        if vector[i] < ecuation.MIN_VALUE:      #If the value goes below the minimum value,
            new_vector.append(ecuation.MIN_VALUE)   #we re-write it to the actual minimum.

        if vector[i] > ecuation.MAX_VALUE:      #If the value goes above the maximum value,
            new_vector.append(ecuation.MAX_VALUE)   #we re-write it to the actual maximum.

        if ecuation.MIN_VALUE <= vector[i] <= ecuation.MAX_VALUE:   #If the value is acceptable,
            new_vector.append(vector[i])                            #we just let it as it is.
        
    return new_vector


#The actual Differential Evolution Algorithm.
def differentialEvolution(ecuation, dimensions, individuals, F, c, generations):
    graphArray = np.array([])   #For graphing the results.

    #We begin by generatin a population. Each individual has a vector with
    population = []     #as much spaces as dimensions for the ecuation, with values between the ecuation bounds.
    for i in range(0, individuals):
        individual = []
        for j in range(dimensions):
            individual.append(random.uniform(ecuation.MIN_VALUE, ecuation.MAX_VALUE))
        population.append(individual)

    for i in range(0, generations):
        print('GENERATION:',i)
        fitness_scores = [] #We catch the best fitness here.
        
        for j in range(0, individuals):
            #We start with the actual mutation.
            #We begin by selecting 3 random individuals that are also different from the iteration individual.
            candidates = list(range(0, individuals))
            candidates.remove(j)
            random_candidate = random.sample(candidates, 3)

            x1 = population[random_candidate[0]]
            x2 = population[random_candidate[1]]
            x3 = population[random_candidate[2]]
            actual_individual = population[j]

            #We get the difference between two vectors to create the mutant vector.
            difference = [x2_i - x3_i for x2_i, x3_i in zip(x2, x3)]

            #We multiply the difference by the mutation factor (F) and add to x1
            mutant_vector = [x1_i + F * difference_i for x1_i, difference_i in zip(x1, difference)]
            
            #We make sure the vector won't go out of the solving problem bounds.
            mutant_vector = ensure_bounds(mutant_vector, ecuation)

            #Recombination of the vectors. If a random value goes below our "c", we change the value.
            trial_vector = []
            for k in range(len(actual_individual)):
                crossover = random.random()
                if crossover <= c:
                    trial_vector.append(mutant_vector[k])

                else:
                    trial_vector.append(actual_individual[k])
                    
            #Selection of the best individual.
            trial_vector_fitness  = ecuation.fitness(trial_vector)
            actual_individual_fitness = ecuation.fitness(actual_individual)

            if trial_vector_fitness < actual_individual_fitness:
                population[j] = trial_vector
                fitness_scores.append(trial_vector_fitness)

            else:
                fitness_scores.append(actual_individual_fitness)

        generation_best = population[fitness_scores.index(min(fitness_scores))]     # solution of best individual
        print(generation_best, ecuation.fitness(generation_best), '\n')
        if i % 100 == 0 :
            graphArray = np.append(graphArray, [ecuation.fitness(generation_best)])

    return graphArray