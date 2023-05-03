import numpy as np
import random

from Lab4.cerinta1Functions.schwefel_1 import schwefel_1


# Define the genetic algorithm
def genetic_algorithm(pop_size, num_generations, crossover_prob, mutation_prob, num_parents):
    # Initialize the population -> pairs (x, y) between -500 and 500
    population = np.random.uniform(-500, 500, size=(pop_size, 2))
    average_fitness = 0
    best_fitness = 0
    for generation in range(num_generations):
        # Calculate the fitness for each individual in the population
        fitness = np.array([schwefel_1(individual) for individual in population])

        # Select the parents
        # Sort the population by fitness value: The population is sorted in ascending order of
        # fitness values. The reason for sorting the population is to select the fittest individuals as parents for
        # the next generation. (so that the best individuals are not lost)

        parents = population[np.argsort(fitness)[:num_parents]]

        # Create the next generation
        new_population = []
        while len(new_population) < pop_size:
            # Select two parents
            parent1, parent2 = random.choices(parents, k=2)

            # In this implementation, the crossover operation used is called "single-point crossover". Here's how it
            # works:
            #
            # Two parents are selected randomly from the selected parents for the next generation.
            #
            # A random index is chosen between 0 and the length of the parents' chromosome.
            #
            # The chromosome of the first parent from index 0 to the chosen index is concatenated with the chromosome
            # of the second parent from the chosen index to the end.
            #
            # The resulting chromosome is the offspring produced by crossover.

            # Crossover
            if random.random() < crossover_prob:
                child = np.array([parent1[0], parent2[1]])
            else:
                child = np.array([parent1[0], parent1[1]])

            # In this implementation, the mutation operation used is a simple "Gaussian mutation". Here's how it works:
            #
            # For each gene in the chromosome of an offspring, a random number is generated from a normal
            # distribution with mean 0 and standard deviation of 10.
            #
            # The random number generated in step 1 is added to the gene's value to produce a new value.
            #
            # The resulting chromosome is the offspring produced by mutation.
            # Mutate
            if random.random() < mutation_prob:
                child += np.random.normal(0, 10, size=2)

            # Add the child to the new population
            new_population.append(child)

        # Replace the old population with the new population
        population = np.array(new_population)

        # Print the best individual in the population
        best_fitness = np.min(fitness)
        best_individual = population[np.argmin(fitness)]
        average_fitness += best_fitness
        print(f"Generation {generation}: Best fitness = {best_fitness:.2f}, Best individual = {best_individual}")

    return best_fitness, average_fitness / num_generations
