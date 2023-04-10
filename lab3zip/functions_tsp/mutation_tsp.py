import random


# Mutate a solution by swapping two cities
def mutation_tsp(solution, mutation_rate):
    if random.random() < mutation_rate:
        a, b = random.sample(range(len(solution)), 2)
        solution[a], solution[b] = solution[b], solution[a]
    return solution
