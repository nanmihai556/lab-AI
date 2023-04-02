import random

from Lab3.functions.crossover import crossover
from Lab3.functions.evaluate import evaluate
from Lab3.functions.initialize import initialize
from Lab3.functions.mutation import mutation

# Problem data
objects = [("Object 1", 5, 10), ("Object 2", 7, 13), ("Object 3", 8, 17),
           ("Object 4", 4, 9), ("Object 5", 3, 7), ("Object 6", 2, 5),
           ("Object 7", 6, 11), ("Object 8", 1, 3), ("Object 9", 9, 19)]


# Evolutionary algorithm
def evolutionary_algorithm(weights, values, max_capacity, population_size, generations, crossover_rate, mutation_rate):
    # Initialization of the population
    population = [initialize(weights) for _ in range(population_size)]

    # Evolution loop
    for generation in range(generations):
        # Evaluation of the population
        fitness = [evaluate(solution, weights, values, max_capacity) for solution in population]

        # Selection of the parents (random)
        # fitness_sum = sum(fitness)
        parent1 = population[random.choices(range(population_size), weights=fitness)[0]]
        parent2 = population[random.choices(range(population_size), weights=fitness)[0]]

        # Crossover and mutation of the children
        if random.random() < crossover_rate:
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            population += [child1, child2]

        # Elitism: selection of the best solutions for the next generation
        population = [population[i] for i in
                      sorted(range(len(fitness)), key=lambda k: fitness[k], reverse=True)[:population_size]]

        # Display of the best solution of the current generation
        print("Generation ", generation, ": ", max(fitness))

    # Return of the best solution found
    best_solution = population[fitness.index(max(fitness))]
    best_solution_value = evaluate(best_solution, weights, values, max_capacity)
    return best_solution, best_solution_value

