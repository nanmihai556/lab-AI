import random
import numpy as np
import pandas as pd

from Lab3.functions.crossover import crossover
from Lab3.functions.crossover_tsp import crossover_tsp
from Lab3.functions_tsp.evaluate_tsp import evaluate_tsp
from Lab3.functions_tsp.initialize_random_solution import initialize_random_solution
from Lab3.functions_tsp.mutation_tsp import mutation_tsp


def evolutionary_algorithm_tsp(coords, population_size, generations, crossover_rate, mutation_rate):
    # Initialization of the population (random)
    population = [initialize_random_solution(coords) for _ in range(population_size)]
    fitnesses = []
    # Evolution loop
    for generation in range(generations):
        # Evaluation of the population
        fitnesses = [evaluate_tsp(solution, coords) for solution in population]

        # Selection of the parents (roulette wheel selection)
        parent1 = population[random.choices(range(population_size), weights=fitnesses)[0]]
        parent2 = population[random.choices(range(population_size), weights=fitnesses)[0]]

        # Crossover and mutation of the children
        aux_population_size = population_size
        while aux_population_size:
            if random.random() < crossover_rate:
                child1, child2 = crossover_tsp(parent1, parent2)
                child1 = mutation_tsp(child1, mutation_rate)
                child2 = mutation_tsp(child2, mutation_rate)
                population += [child1, child2]
            aux_population_size -= 2

        # Elitism: selection of the best solutions for the next generation
        # selectie proportionala cu fitness-ul
        population = [population[i] for i in
                      sorted(range(len(fitnesses)), key=lambda k: fitnesses[k], reverse=True)[:population_size]]

    # Return of the best solution found
    best_solution = population[fitnesses.index(max(fitnesses))]
    best_solution_value = evaluate_tsp(best_solution, coords)
    return best_solution, best_solution_value
