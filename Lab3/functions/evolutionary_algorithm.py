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


def evolutionary_algorithm(weights, values, max_capacity, population_size, generations, crossover_rate, mutation_rate):
    population = [initialize(weights) for _ in range(population_size)]  # random solutions

    # Evolution loop
    for generation in range(generations):

        fitnesses = [evaluate(solution, weights, values, max_capacity) for solution in population]  # array of fitnesses

        # Selection of the parents (random) based on fitness value (the higher the fitness, the higher the probability
        # to be chosen

        parent1 = population[random.choices(range(population_size), weights=fitnesses)[0]]
        parent2 = population[random.choices(range(population_size), weights=fitnesses)[0]]

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

    # Return of the best solution found
    best_solution = population[fitnesses.index(max(fitnesses))]
    best_solution_value = evaluate(best_solution, weights, values, max_capacity)
    return best_solution, best_solution_value
