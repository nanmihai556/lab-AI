import math
import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


def read_data(file_name):
    df = pd.read_csv(file_name, delim_whitespace=True, header=None, skiprows=6)
    cities = df.iloc[:, :2].values.tolist()
    dist_mat = np.zeros((len(cities), len(cities)), dtype=int)
    for i in range(len(cities)):
        for j in range(len(cities)):
            dist_mat[i][j] = distance(cities[i], cities[j])
    return cities, dist_mat


def tabu_search(file_name, max_iter, tabu_size):
    cities, dist_mat = read_data(file_name)
    n = len(cities)

    # Initialize current and best solution
    current_sol = random.sample(range(n), n)
    best_sol = current_sol.copy()
    best_cost = sum([dist_mat[current_sol[i - 1]][current_sol[i]] for i in range(n)])

    # Initialize tabu list
    tabu_list = []

    # Set maximum number of iterations
    iter_count = 0

    # Start the algorithm
    while iter_count < max_iter:
        # Generate a new neighbor solution
        neighbor = current_sol.copy()
        i, j = sorted(random.sample(range(n), 2))
        neighbor[i:j + 1] = reversed(neighbor[i:j + 1])
        neighbor_cost = sum([dist_mat[neighbor[i - 1]][neighbor[i]] for i in range(n)])

        # Check if neighbor solution is better than current solution
        if neighbor_cost < best_cost:
            best_sol = neighbor.copy()
            best_cost = neighbor_cost

        # Check if neighbor solution is allowed in tabu list
        elif neighbor not in tabu_list:
            current_sol = neighbor.copy()

            # Add neighbor solution to tabu list
            tabu_list.append(current_sol.copy())

            # Remove oldest solution from tabu list
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)

        # Increment the iteration counter
        iter_count += 1

    # Return the best solution and its cost
    return best_sol, best_cost
