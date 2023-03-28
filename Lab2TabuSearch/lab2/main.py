# 1. Tabu search on knapscack problem
# 2. Simulatd Annealing/ Tabu search on TSP problem
# pr124.tsp
from Lab2TabuSearch.tabu_search_tsp import tabu_search_tsp


def start():
    number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
    best_of_all = float('inf')
    average_of_all = 0
    for l in range(0, 9):
        for _ in range(number_of_solutions):
            average = 0
            best_solution, best_distance = tabu_search_tsp("pr124.tsp", tabu_list_size=10, max_iterations=5)
            print('Best solution:', best_solution)
            print('Best distance:', best_distance)
            average += best_distance
            if best_distance < best_of_all:
                best_of_all = best_distance
            average = average / number_of_solutions
            average_of_all += average
    print("Best of all: " + str(best_of_all))
    print("Average of all: " + str(average_of_all))


start()
