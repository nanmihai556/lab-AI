from Lab4.cerinta1Functions.genetic_algorithm import genetic_algorithm

population_size = int(input('Enter the population size: \n'))  # basic -> 100
number_of_generations = int(input('Enter number of generations to be generated: \n'))
crossover_rate = float(input('Enter crossover rate: \n'))  # de obicei intre 0.6 si 0.9
mutation_rate = float(input('Enter mutation rate: \n'))  # incepem cu 0.01 si crestem gradual
num_parents = int(input('Enter number of parents: \n'))

# The num_parents parameter is usually set to a value that is smaller than the population size, since the same
# individual can be selected as a parent multiple times (i.e., the selection process is done with replacement). This
# helps to maintain diversity in the population and prevent premature convergence of the algorithm.

# default : pop_size=100, num_generations=100, crossover_prob=0.8, mutation_prob=0.1, num_parents=10
best_of_all = 999999999
average_of_all = 0
for l in range(0, 9):
    best, average = genetic_algorithm(pop_size=population_size, num_generations=number_of_generations, crossover_prob=crossover_rate,
                      mutation_prob=mutation_rate, num_parents=10)
    if(best < best_of_all):
        best_of_all = best
    average_of_all += average

print(f"Best of all: {best_of_all}", f"\n Average of all: {average_of_all / 10}")
