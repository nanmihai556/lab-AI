import random


# Mutate a solution by swapping two cities
def mutation_tsp(solution):
    a, b = random.sample(range(len(solution)), 2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution
