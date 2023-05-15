# Sure, I'd be happy to explain Ant Colony Optimization (ACO)!
#
# Ant Colony Optimization is a metaheuristic algorithm inspired by the behavior of ants searching for food. When ants
# forage for food, they leave a trail of pheromones that other ants can follow. The more ants that follow the trail,
# the stronger the trail becomes due to the accumulation of pheromones. At the same time, the pheromones evaporate
# over time, so the strength of the trail diminishes if it is not reinforced by the ants.
#
# In ACO, the problem to be solved is represented as a graph, where the nodes correspond to the possible solutions
# and the edges correspond to the transitions between them. Each ant traverses the graph by probabilistically
# choosing its next node based on the pheromone levels and a heuristic function that takes into account the
# desirability of each node.
#
# As the ants move through the graph, they deposit pheromones on the edges they traverse, with the amount of
# pheromone deposited proportional to the quality of the solution obtained. This reinforces the edges corresponding
# to good solutions and biases future ants towards those solutions. At the same time, the pheromones evaporate over
# time, which prevents the algorithm from getting stuck in local optima.
#
# The algorithm terminates when a stopping criterion is met, such as a fixed number of iterations or a certain level
# of convergence. The best solution found is the path corresponding to the highest amount of pheromone.
#
# ACO can be implemented in different ways, with different strategies for updating the pheromone levels and choosing
# the next node to visit. Two common variants are Ant System (AS) and Ant Colony System (ACS).
#
# In Ant System, the pheromone levels are updated by adding a fixed amount of pheromone to the edges corresponding to
# the best solution found so far. The next node to visit is chosen probabilistically based on the pheromone levels
# and a heuristic function that takes into account the distance between nodes.
#
# In Ant Colony System, the pheromone levels are updated by adding a variable amount of pheromone to the edges
# corresponding to the best solution found so far and to the edges traversed by the ants that find good solutions.
# The next node to visit is chosen probabilistically based on the pheromone levels, a heuristic function,
# and an additional parameter called the "trail attractiveness" that biases the choice towards the best solution
# found so far.
#
# ACO has been successfully applied to a wide range of combinatorial optimization problems, including the Traveling
# Salesman Problem, the Vehicle Routing Problem, and the Job Shop Scheduling Problem.

from Lab4.cerinta3Functions.ant_system import ant_system


number_of_ants = int(input('Enter number of ants: \n'))
number_of_iterations = int(input('Enter number of iterations: \n'))
alpha = float(input('Enter alpha: \n'))
beta = float(input('Enter beta: \n'))
evaporation_rate = float(input('Enter evaporation rate: \n'))

# num_ants=10, num_iterations=100, alpha=1, beta=5, evaporation_rate=0.5
best_tour, best_tour_length = ant_system(num_ants=number_of_ants, num_iterations=number_of_iterations,
                                         alpha=alpha, beta=beta, evaporation_rate=evaporation_rate)

print("Best tour: \n", best_tour)
print("Best tour length:", best_tour_length)
