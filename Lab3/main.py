import numpy as np
import matplotlib.pyplot as plt

from Lab2TabuSearch.read_data import read_data
from Lab3.functions_tsp.evolutionary_algorithm_tsp import evolutionary_algorithm_tsp

coords = read_data('pr124.tsp')

population_size = int(input('Enter the population size: \n'))
number_of_generations = int(input('Enter number of generations to be generated: \n'))
crossover_rate = float(input('Enter crossover rate: \n'))
mutation_rate = float(input('Enter mutation rate: \n'))

best_of_all = 0
average_of_all = 0
best_solutions_array = []
average_solutions_array = []
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
    print("Average: ", average)
    best_solutions_array.append(1 / best_solution_value)


best_solutions_array = np.array(best_solutions_array)
average_solutions_array.append([average_of_all])
average_solutions_array = np.array(average_solutions_array)

print("Best of all: " + str(best_of_all))
print("Average of all: " + str(average_of_all))

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the best solutions as a blue line
ax.plot(best_solutions_array, color='blue', label='Best')

# Add a title and axis labels
ax.set_title('Evolutionary TSP Algorithm Performance')
ax.set_xlabel('Generation')
ax.set_ylabel('Solution Quality')

# Add a legend
ax.legend()

# Show the plot
plt.show()
