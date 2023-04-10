from Lab2TabuSearch.read_data import read_data
from Lab3.functions_tsp.evolutionary_algorithm_tsp import evolutionary_algorithm_tsp

coords = read_data('pr124.tsp')

population_size = int(input('Enter the population size: \n'))
number_of_generations = int(input('Enter number of generations to be generated: \n'))
crossover_rate = float(input('Enter crossover rate: \n'))
mutation_rate = float(input('Enter mutation rate: \n'))

best_of_all = 0
average_of_all = 0
for l in range(0, 9):
    average = 0
    best_solution, best_solution_value = evolutionary_algorithm_tsp(coords, population_size, number_of_generations,
                                                                    crossover_rate, mutation_rate)
    average += 1 / best_solution_value
    if best_solution_value > best_of_all:
        best_of_all = 1 / best_solution_value
    average = average / 10
    average_of_all += average
    print("Best solution found: ", best_solution)
    print("Best solution distance: ", 1 / best_solution_value)

print("Best of all: " + str(best_of_all))
print("Average of all: " + str(average_of_all))
