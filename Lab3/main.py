from Lab2TabuSearch.read_data import read_data
from Lab3.functions_tsp.evolutionary_algorithm_tsp import evolutionary_algorithm_tsp

# Load TSP data
coords = read_data('pr124.tsp')

# Set algorithm parameters

population_size = int(input('Enter the population size: \n'))  # basic -> 100
number_of_generations = int(input('Enter number of generations to be generated: \n'))
crossover_rate = float(input('Enter crossover rate: \n'))  # de obicei intre 0.6 si 0.9
mutation_rate = float(input('Enter mutation rate: \n'))  # incepem cu 0.01 si crestem gradual

# Run evolutionary algorithm
best_solution, best_solution_value = evolutionary_algorithm_tsp(coords, population_size, number_of_generations,
                                                                crossover_rate, mutation_rate)

# Print results
print("Best solution found: ", best_solution)
print("Best solution distance: ", 1 / best_solution_value)
