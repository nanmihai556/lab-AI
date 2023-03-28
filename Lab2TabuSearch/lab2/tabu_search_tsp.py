import random

from Lab2TabuSearch.distance import distance
from Lab2TabuSearch.generate_initial_solution import generate_initial_solution
from Lab2TabuSearch.read_data import read_data


def tabu_search_tsp(filename, tabu_list_size=15, max_iterations=1000):
    data = read_data(filename)

    n = len(data)

    # Generate initial solution
    # Ordinea in care vor fi vizitate orasele (luata aleator)
    current_solution = generate_initial_solution(n)
    best_solution = current_solution.copy()
    # Initialize tabu list and other variables
    tabu_list = [current_solution]
    iteration = 0

    while iteration < max_iterations:
        # Generate all possible neighboring solutions
        neighbors = []
        for i in range(n-1):
            for j in range(i+1, n):
                neighbor = current_solution.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)

        # Evaluate all neighboring solutions
        best_neighbor = None
        best_neighbor_distance = float('inf')
        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_distance = sum(distance(data[neighbor[i] - 1], data[neighbor[i-1] - 1]) for i in range(n))
                if neighbor_distance < best_neighbor_distance:
                    best_neighbor = neighbor
                    best_neighbor_distance = neighbor_distance

        # If all neighbors are tabu, select first one
        if best_neighbor is None:
            best_neighbor = neighbors[0]
            best_neighbor_distance = sum(distance(data[best_neighbor[i] - 1], data[best_neighbor[i-1] - 1]) for i in range(n))

        # Update current solution
        current_solution = best_neighbor
        tabu_list.append(current_solution)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        # Update best solution
        if best_neighbor_distance < sum(distance(data[best_solution[i] - 1], data[best_solution[i-1] - 1]) for i in range(n)):
            best_solution = best_neighbor.copy()

        iteration += 1

    return best_solution, sum(distance(data[best_solution[i] - 1], data[best_solution[i-1] - 1]) for i in range(n))
