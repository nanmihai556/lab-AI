import numpy as np
from matplotlib import pyplot as plt

from Lab3.functions.evolutionary_algorithm import evolutionary_algorithm
from functions.tabu_search import tabu_search
from functions.generateRandomSolutions import generateRandomSolutions
from functions.randomHillClimbing import randomHillClimbing




weights = [6, 3, 2, 4, 5, 8, 9, 2, 1, 3, 5, 3, 7, 8]
values = [2, 2, 5, 9, 2, 2, 5, 9, 2, 2, 5, 9, 2, 1]
numberOfObjects = 14
backpackCapacity = 50


def start():
    print('a.Knapsack problem')
    print('b.Knapsack problem - Random hill climbing')
    print('c.Knapsack problem - Tabu Search')
    print('d.Knapsack problem - Algoritm Evolutiv')
    type = input()
    if type == 'a':
        print('1. Read from file:')
        print('2. Read from local data')
        x = input()
        if x == '1':
            file = input('Choose file: \n 1. rucsac-20.txt \n 2. rucsac-200.txt \n')
            name_of_file = ''
            if file == '1':
                name_of_file = 'rucsac-20.txt'
            else:
                name_of_file = 'rucsac-200.txt'

            number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
            best_of_all = 999999  # get from file
            average_of_all = 0
            for l in range(0, 9):
                f = open(name_of_file)
                # Read first line of .txt file -> number of objects
                file_number_of_objects = [int(x) for x in next(f).split()][0]
                file_weights = []
                file_values = []

                # Read weights and values from file
                for line in f:
                    object = [int(x) for x in line.split()]
                    if len(object) < 3:
                        break
                    file_weights.append(object[1])
                    file_values.append(object[2])
                # Read last line of file -> backpack capacity
                for line in f:
                    pass
                file_backpack_capacity = int(line)
                [best, average] = generateRandomSolutions(number_of_solutions, file_weights, file_values,
                                                          file_number_of_objects, file_backpack_capacity)
                if best < best_of_all:
                    best_of_all = best
                average_of_all += average
                f.close()
            print("\nBest of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all / number_of_solutions))
        elif x == '2':
            number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
            best_of_all = 999999999
            average_of_all = 0
            for l in range(0, 9):
                best_of_all = backpackCapacity
                [best, average] = generateRandomSolutions(number_of_solutions, weights, values, numberOfObjects,
                                                          backpackCapacity)
                if best < best_of_all:
                    best_of_all = best
                    average_of_all += average
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all / number_of_solutions))
    elif type == 'b':
        print('1. Read from file:')
        print('2. Read from local data')
        x = input()
        if x == '1':
            file = input('Choose file: \n 1. rucsac-20.txt \n 2. rucsac-200.txt \n')
            name_of_file = ''
            if file == '1':
                name_of_file = 'rucsac-20.txt'
            else:
                name_of_file = 'rucsac-200.txt'

            number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
            best_of_all = 9999999  # get from file
            average_of_all = 0
            for l in range(0, 9):
                f = open(name_of_file)
                # Read first line of .txt file -> number of objects
                file_number_of_objects = [int(x) for x in next(f).split()][0]
                file_weights = []
                file_values = []

                # Read weights and values from file
                for line in f:
                    object = [int(x) for x in line.split()]
                    if (len(object) < 3):
                        break
                    file_weights.append(object[1])
                    file_values.append(object[2])
                # Read last line of file -> backpack capacity
                for line in f:
                    pass
                file_backpack_capacity = int(line)
                average = 0
                for m in range(0, number_of_solutions):
                    solution, quality = [], 0
                    try:
                        solution, quality = randomHillClimbing(file_weights, file_values, file_backpack_capacity, 100)
                    except:
                        continue
                    print(str(m) + '.' + str(solution) + " Quality: " + str(quality))
                    average += quality
                    if quality < best_of_all:
                        best_of_all = quality
                average = average / number_of_solutions
                average_of_all += average
                f.close()
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all / number_of_solutions))
        elif x == '2':
            number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
            best_of_all = 999999999
            average_of_all = 0
            # simulare 10 rulari
            for l in range(0, 9):
                average = 0
                for m in range(0, number_of_solutions):
                    solution, quality = [], 0
                    try:
                        solution, quality = randomHillClimbing(weights, values, backpackCapacity, 1000)
                    except:
                        continue
                    print(str(m) + '.' + str(solution) + " Quality: " + str(quality))
                    average += quality
                    if quality < best_of_all:
                        best_of_all = quality
                average = average / number_of_solutions
                average_of_all += average
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all / number_of_solutions))
    elif type == 'c':
        print('1. Read from file:')
        print('2. Read from local data')
        x = input()
        tabu_size = 5
        if x == '1':
            file = input('Choose file: \n 1. rucsac-20.txt \n 2. rucsac-200.txt \n')
            name_of_file = ''
            if file == '1':
                name_of_file = 'rucsac-20.txt'
            else:
                name_of_file = 'rucsac-200.txt'

            number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
            best_of_all = 0  # get from file
            average_of_all = 0
            for l in range(0, 9):
                f = open(name_of_file)
                # Read first line of .txt file -> number of objects
                file_number_of_objects = [int(x) for x in next(f).split()][0]
                file_weights = []
                file_values = []

                # Read weights and values from file
                for line in f:
                    object = [int(x) for x in line.split()]
                    if len(object) < 3:
                        break
                    file_weights.append(object[1])
                    file_values.append(object[2])
                # Read last line of file -> backpack capacity
                for line in f:
                    pass
                file_backpack_capacity = int(line)
                average = 0
                best_solution, best_solution_value = tabu_search(file_weights, file_values, file_backpack_capacity, 100,
                                                                 tabu_size, number_of_solutions)
                average += best_solution_value
                print("Best solution:", best_solution)
                print("Best solution value:", best_solution_value)
                if best_solution_value > best_of_all:
                    best_of_all = best_solution_value
                average = average / number_of_solutions
                average_of_all += average
                f.close()
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all))
        elif x == '2':
            number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
            best_of_all = 0
            average_of_all = 0
            # simulare 10 rulari
            for l in range(0, 9):
                average = 0
                best_solution, best_solution_value = tabu_search(weights, values, backpackCapacity, 100, tabu_size,
                                                                 number_of_solutions)
                average += best_solution_value
                print("Best solution:", best_solution)
                print("Best solution value:", best_solution_value)

                average = average / number_of_solutions
                average_of_all += average
                if best_solution_value > best_of_all:
                    best_of_all = best_solution_value
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all))
    elif type == 'd':
        print('1. Read from file:')
        print('2. Read from local data')
        x = input()
        if x == '1':
            file = input('Choose file: \n 1. rucsac-20.txt \n 2. rucsac-200.txt \n')
            name_of_file = ''
            if file == '1':
                name_of_file = 'rucsac-20.txt'
            else:
                name_of_file = 'rucsac-200.txt'

            population_size = int(input('Enter the population size: \n'))  # basic -> 100
            number_of_generations = int(input('Enter number of generations to be generated: \n'))
            crossover_rate = float(input('Enter crossover rate: \n'))  # de obicei intre 0.6 si 0.9
            mutation_rate = float(input('Enter mutation rate: \n'))  # incepem cu 0.01 si crestem gradual
            best_of_all = 0  # get from file
            average_of_all = 0
            best_solutions_array = []
            for l in range(0, 9):
                f = open(name_of_file)
                # Read first line of .txt file -> number of objects
                file_number_of_objects = [int(x) for x in next(f).split()][0]
                file_weights = []
                file_values = []

                # Read weights and values from file
                for line in f:
                    object = [int(x) for x in line.split()]
                    if len(object) < 3:
                        break
                    file_weights.append(object[1])
                    file_values.append(object[2])
                # Read last line of file -> backpack capacity
                for line in f:
                    pass
                file_backpack_capacity = int(line)
                average = 0
                best_solution, best_solution_value = evolutionary_algorithm(
                    file_weights, file_values, file_backpack_capacity, population_size=population_size,
                    generations=number_of_generations, crossover_rate=crossover_rate, mutation_rate=mutation_rate)
                average += best_solution_value
                print("Best solution:", best_solution)
                print("Best solution value:", best_solution_value)
                best_solutions_array.append(best_solution_value)
                if best_solution_value > best_of_all:
                    best_of_all = best_solution_value
                average = average / 10
                average_of_all += average
                best_solutions_array.append(1 / best_solution_value)
                f.close()
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all))
            best_solutions_array = np.array(best_solutions_array)
            # Create a new figure and axis
            fig, ax = plt.subplots()

            # Plot the best solutions as a blue line
            ax.plot(best_solutions_array, color='blue', label='Best')

            # Add a title and axis labels
            ax.set_title('Knapsack AE Algorithm Performance')
            ax.set_xlabel('Generation')
            ax.set_ylabel('Solution Quality')

            # Add a legend
            ax.legend()

            # Show the plot
            plt.show()

        elif x == '2':
            population_size = int(input('Enter the population size: \n'))  # basic -> 100
            number_of_generations = int(input('Enter number of generations to be generated: \n'))
            crossover_rate = float(input('Enter crossover rate: \n'))  # de obicei intre 0.6 si 0.9
            mutation_rate = float(input('Enter mutation rate: \n'))  # incepem cu 0.01 si crestem gradual
            best_of_all = 0
            average_of_all = 0
            # simulare 10 rulari
            best_solutions_array = []
            for l in range(0, 9):
                average = 0
                best_solution, best_solution_value = evolutionary_algorithm(
                    weights, values, backpackCapacity, population_size=population_size,
                    generations=number_of_generations, crossover_rate=crossover_rate, mutation_rate=mutation_rate)

                average += best_solution_value
                print("Best solution:", best_solution)
                print("Best solution value:", best_solution_value)
                best_solutions_array.append(best_solution_value)
                average = average / 10
                average_of_all += average
                if best_solution_value > best_of_all:
                    best_of_all = best_solution_value
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all))
            best_solutions_array = np.array(best_solutions_array)

            # Create a new figure and axis
            fig, ax = plt.subplots()

            # Plot the best solutions as a blue line
            ax.plot(best_solutions_array, color='blue', label='Best')

            # Add a title and axis labels
            ax.set_title('Knapsack AE Algorithm Performance')
            ax.set_xlabel('Generation')
            ax.set_ylabel('Solution Quality')

            # Add a legend
            ax.legend()

            # Show the plot
            plt.show()




start()

