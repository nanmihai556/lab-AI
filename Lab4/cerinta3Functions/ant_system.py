import random

import numpy as np

from Lab4.cerinta3Functions.read_tsp_file import read_tsp_file


def ant_system(num_ants, num_iterations, alpha, beta, evaporation_rate):
    dist_matrix = read_tsp_file("pr124.tsp")

    pheromone_matrix = np.ones(dist_matrix.shape) / dist_matrix.shape[0]

    best_tour = None
    best_tour_length = np.inf

    for iteration in range(num_iterations):
        ants = np.zeros((num_ants, dist_matrix.shape[0]), dtype=int)

        for ant in range(num_ants):
            visited_cities = set()
            current_city = random.randint(0, dist_matrix.shape[0] - 1)
            visited_cities.add(current_city)
            ants[ant, 0] = current_city

            for i in range(1, dist_matrix.shape[0]):
                unvisited_cities = set(range(dist_matrix.shape[0])) - visited_cities
                pheromone_levels = pheromone_matrix[current_city, list(unvisited_cities)]
                distances = dist_matrix[current_city, list(unvisited_cities)]
                probabilities = np.power(pheromone_levels, alpha) * np.power(1 / distances, beta)
                probabilities /= np.sum(probabilities)

                next_city = random.choices(list(unvisited_cities), weights=probabilities)[0]
                visited_cities.add(next_city)
                ants[ant, i] = next_city
                current_city = next_city

            tour_length = np.sum(dist_matrix[ants[ant], np.roll(ants[ant], -1)])
            if tour_length < best_tour_length:
                best_tour = ants[ant]
                best_tour_length = tour_length

        pheromone_matrix *= (1 - evaporation_rate)
        for ant in range(num_ants):
            for i in range(dist_matrix.shape[0] - 1):
                pheromone_matrix[ants[ant, i], ants[ant, i + 1]] += 1 / dist_matrix[ants[ant, i], ants[ant, i + 1]]
            pheromone_matrix[ants[ant, -1], ants[ant, 0]] += 1 / dist_matrix[ants[ant, -1], ants[ant, 0]]

    return best_tour, best_tour_length
