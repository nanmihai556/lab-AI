from Lab2TabuSearch.read_data import read_data
from Lab3.functions_tsp.evolutionary_algorithm_tsp import evolutionary_algorithm_tsp

# Load TSP data
coords = read_data('pr124.tsp')

# Set algorithm parameters
population_size = 50
generations = 100
crossover_rate = 0.8
mutation_rate = 0.2

# Run evolutionary algorithm
best_solution, best_solution_value = evolutionary_algorithm_tsp(coords, population_size, generations,
                                                                crossover_rate, mutation_rate)

# Print results
print("Best solution found: ", best_solution)
print("Best solution distance: ", 1 / best_solution_value)
