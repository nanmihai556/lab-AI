import numpy as np


def crossover_tsp(parent1, parent2):
    # Get the length of the parent tours
    tour_length = len(parent1)

    # Initialize the child tours as empty arrays
    child1 = np.zeros(tour_length, dtype=int)
    child2 = np.zeros(tour_length, dtype=int)

    # Select a random crossover point
    point = np.random.randint(0, tour_length)

    # Initialize a set to keep track of cities used in child1
    child1_cities = set()

    # Copy cities from parent1 up to the crossover point to child1
    for i in range(point):
        child1[i] = parent1[i]
        child1_cities.add(parent1[i])

    # Copy cities from parent2 to child1, skipping any cities already used
    child1_index = point
    for city in parent2:
        if city not in child1_cities:
            child1[child1_index] = city
            child1_cities.add(city)
            child1_index += 1

    # Initialize a set to keep track of cities used in child2
    child2_cities = set()

    # Copy cities from parent2 up to the crossover point to child2
    for i in range(point):
        child2[i] = parent2[i]
        child2_cities.add(parent2[i])

    # Copy cities from parent1 to child2, skipping any cities already used
    child2_index = point
    for city in parent1:
        if city not in child2_cities:
            child2[child2_index] = city
            child2_cities.add(city)
            child2_index += 1

    return child1, child2
