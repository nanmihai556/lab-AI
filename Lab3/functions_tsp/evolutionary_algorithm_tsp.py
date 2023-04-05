import random
import numpy as np
import pandas as pd

from Lab3.functions.crossover import crossover
from Lab3.functions_tsp.evaluate_tsp import evaluate_tsp
from Lab3.functions_tsp.initialize_random_solution import initialize_random_solution
from Lab3.functions_tsp.mutation_tsp import mutation_tsp


def evolutionary_algorithm_tsp(coords, population_size, generations, crossover_rate, mutation_rate):
    # Initialization of the population (random)
    population = [initialize_random_solution(coords) for _ in range(population_size)]

    # Evolution loop
    for generation in range(generations):
        # Evaluation of the population
        fitnesses = [evaluate_tsp(solution, coords) for solution in population]

        # Selection of the parents (roulette wheel selection)
        parent1 = population[random.choices(range(population_size), weights=fitnesses)[0]]
        parent2 = population[random.choices(range(population_size), weights=fitnesses)[0]]

        # Crossover and mutation of the children
        if random.random() < crossover_rate:
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation_tsp(child1)
            child2 = mutation_tsp(child2)
            population += [child1, child2]

        # Elitism: selection of the best solutions for the next generation
        fitness_df = pd.DataFrame({'solution': population, 'fitness': fitnesses})
        fitness_df = fitness_df.sort_values(by=['fitness'], ascending=False)
        population = list(fitness_df['solution'].values)[:population_size]

        # Display of the best solution of the current generation
        print("Generation ", generation, ": ", max(fitnesses))

    # Return of the best solution found
    best_solution = population[fitnesses.index(max(fitnesses))]
    best_solution_value = evaluate_tsp(best_solution, coords)
    return best_solution, best_solution_value
