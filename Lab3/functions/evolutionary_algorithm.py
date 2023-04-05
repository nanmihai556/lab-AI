# 1. Să se implementeze un algoritm evolutiv pentru problema rucsacului.
# a. Codificare binară
# b. Operatori specifici (ȋncrucişare, mutație)
# c. Algoritm şi parametrizare
# d. Experimente pe cele două instanţe primite la Tema 1


# 2. Să se implementeze un algoritm evolutiv pentru problema comis-voiajorului.
# a. Codificare prin permutări
# b. Operatori specifici (ȋncrucişare, mutație)
# c. Algoritm şi parametrizare
# d. Experimente pe instanţa primită la Tema 2

# Algoritmul evolutiv pentru problema rucsacului va fi implementat pe baza unei reprezentări binare,
# repararea indivizilor care reprezintă soluţii nevalide (pentru a respecta capacitatea rucsacului) şi o
# funcţie de fitness ce calculeaza valoarea totală pusă în rucsac (ce trebuie maximizată).
# Algoritmul evolutiv pentru problema TSP va fi implementat pe baza unei reprezentări prin permutări,
# folosirea unor operatori de încrucişare şi mutație care generează soluții valide şi o funcție de fitness
# ce calculează distanța totală parcursă (ce trebuie minimizată).
# Componentele algoritmului sunt:
#  Generare populaţie iniţială aleator (populaţie P).
#  Selecţie părinţi.
#  Generare descendenţi: încrucişare şi mutaţie (populaţie O).
#  Selecţie supravieţuitori: cei mai buni size(P) din P+O.
#  Parametri algoritm: mărimea populaţiei, numărul de generaţii, probabilitatea de încrucişare,
# probabilitatea de mutaţie.

import random

from Lab3.functions.crossover import crossover
from Lab3.functions.evaluate import evaluate
from Lab3.functions.initialize import initialize
from Lab3.functions.mutation import mutation


# Problem data
# objects = [("Object 1", 5, 10), ("Object 2", 7, 13), ("Object 3", 8, 17),
#            ("Object 4", 4, 9), ("Object 5", 3, 7), ("Object 6", 2, 5),
#            ("Object 7", 6, 11), ("Object 8", 1, 3), ("Object 9", 9, 19)]


# Evolutionary algorithm
def evolutionary_algorithm(weights, values, max_capacity, population_size, generations, crossover_rate, mutation_rate):
    # Initialization of the population (random)
    population = [initialize(weights) for _ in range(population_size)]  # random solutions

    # Evolution loop
    for generation in range(generations):  # while (t < M) do
        # Evaluation of the population
        fitnesses = [evaluate(solution, weights, values, max_capacity) for solution in population]  # array of fitnesses

        # Selection of the parents (random) based on fitness value (the higher the fitness, the higher the probability
        # to be chosen

        # fitness_sum = sum(fitness)

        parent1 = population[random.choices(range(population_size), weights=fitnesses)[0]]
        parent2 = population[random.choices(range(population_size), weights=fitnesses)[0]]

        # Crossover and mutation of the children

        # A common range for the crossover rate is between 0.6 and 0.9, but the optimal value can vary depending on
        # the problem. A value of 1.0 would mean that all pairs of parents will always undergo crossover,
        # which can be useful for certain problems but may also cause the algorithm to converge too quickly or not
        # explore enough of the search space. It is common to experiment with different values of the crossover rate
        # and observe the performance of the algorithm. The performance can be evaluated by monitoring the fitness of
        # the best solution found, the diversity of the population, and the convergence rate. Adjusting the crossover
        # rate can be done by hand, or by using adaptive techniques that adjust the value of the crossover rate based
        # on the performance of the algorithm during the optimization process.

        # In general, a high mutation rate can increase the exploration of the search space, but may also decrease
        # the stability of the algorithm and cause the algorithm to converge more slowly. On the other hand,
        # a low mutation rate can increase the stability of the algorithm, but may also limit the diversity of the
        # population and cause the algorithm to converge to suboptimal solutions.
        #
        # A common rule of thumb for setting the mutation rate is to start with a small value, such as 0.01,
        # and gradually increase or decrease it based on the performance of the algorithm. If the algorithm is not
        # exploring the search space enough, the mutation rate can be increased, and if the algorithm is converging
        # too quickly to suboptimal solutions, the mutation rate can be decreased.
        #
        # It's worth noting that the optimal mutation rate can also vary depending on the type of mutation operator
        # used. For example, a mutation operator that swaps two elements in the solution may require a different
        # mutation rate than a mutation operator that adds or removes an element from the solution.

        if random.random() < crossover_rate:
            # random index => copy first child array to the index, then the second child
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            population += [child1, child2]

        # Elitism: selection of the best solutions for the next generation
        # selectie proportionala cu fitness-ul
        population = [population[i] for i in
                      sorted(range(len(fitnesses)), key=lambda k: fitnesses[k], reverse=True)[:population_size]]

        # Display of the best solution of the current generation
        # print("Generation ", generation, ": ", max(fitnesses))

    # Return of the best solution found
    best_solution = population[fitnesses.index(max(fitnesses))]
    best_solution_value = evaluate(best_solution, weights, values, max_capacity)
    return best_solution, best_solution_value
