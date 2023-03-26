# 1. Tabu search on knapscack problem
# 2. Simulatd Annealing/ Tabu search on TSP problem
# pr124.tsp
from Lab2TabuSearch.tabu_search_tsp import tabu_search_tsp


def start():
    best_solution, best_distance = tabu_search_tsp("pr124.tsp", tabu_list_size=10, max_iterations=5)
    print('Best solution:', best_solution)
    print('Best cost:', best_distance)


start()
