from Laborator1NanMihai.functions.tabu_search import tabu_search
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

                best_solution, best_solution_value = tabu_search(weights, values, file_backpack_capacity, 100, 5,
                                                                 number_of_solutions)
                print("Best solution:", best_solution)
                print("Best solution value:", best_solution_value)
                if(best_solution_value > best_of_all):
                    best_of_all = best_solution_value
                average = average / 10
                average_of_all += average
                f.close()
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all / number_of_solutions))
        elif x == '2':
            number_of_solutions = int(input('Enter number of solutions to be generated: \n'))
            best_of_all = 0
            average_of_all = 0
            # simulare 10 rulari
            for l in range(0, 9):
                average = 0
                best_solution, best_solution_value = tabu_search(weights, values, backpackCapacity, 100, 5,
                                                                 number_of_solutions)
                print("Best solution:", best_solution)
                print("Best solution value:", best_solution_value)

                average = average / 10
                average_of_all += average
                if (best_solution_value > best_of_all):
                    best_of_all = best_solution_value
            print("Best of all: " + str(best_of_all))
            print("Average of all: " + str(average_of_all / number_of_solutions))


start()

