from functions.generateRandomSolutions import generateRandomSolutions
from functions.randomHillClimbing import randomHillClimbing

weights = [6, 3, 2, 4, 5, 8, 9, 2, 1, 3, 5, 3, 7, 8]
values = [2, 2, 5, 9, 2, 2, 5, 9, 2, 2, 5, 9, 2, 1]
numberOfObjects = 14
backpackCapacity = 50


def start():
    print('a.Knapsack problem')
    print('b.Knapsack problem - Random hill climbing')
    type = input()
    if type == 'a':
        print('1. Read from file:')
        print('2. Read from local data')
        x = input()
        if x == '1':
            file = input('Choose file: \n 1. rucsac-20.txt \n 2. rucsac-200.txt \n')
            nameOfFile = ''
            if file == '1':
                nameOfFile = 'rucsac-20.txt'
            else:
                nameOfFile = 'rucsac-200.txt'

            numberOfSolutions = int(input('Enter number of solutions to be generated: \n'))
            bestOfAll = 999999  # get from file
            averageOfAll = 0
            for l in range(0, 9):
                f = open(nameOfFile)
                # Read first line of .txt file -> number of objects
                fileNumberOfObjects = [int(x) for x in next(f).split()][0]
                fileWeights = []
                fileValues = []

                # Read weights and values from file
                for line in f:
                    object = [int(x) for x in line.split()]
                    if len(object) < 3:
                        break
                    fileWeights.append(object[1])
                    fileValues.append(object[2])
                # Read last line of file -> backpack capacity
                for line in f:
                    pass
                fileBackpackCapacity = int(line)
                [best, average] = generateRandomSolutions(numberOfSolutions, fileWeights, fileValues,
                                                          fileNumberOfObjects, fileBackpackCapacity)
                if best < bestOfAll:
                    bestOfAll = best
                averageOfAll += average
                f.close()
            print("\nBest of all: " + str(bestOfAll))
            print("Average of all: " + str(averageOfAll / numberOfSolutions))
        elif x == '2':
            numberOfSolutions = int(input('Enter number of solutions to be generated: \n'))
            bestOfAll = 999999999
            averageOfAll = 0
            for l in range(0, 9):
                bestOfAll = backpackCapacity
                [best, average] = generateRandomSolutions(numberOfSolutions, weights, values, numberOfObjects,
                                                          backpackCapacity)
                if best < bestOfAll:
                    bestOfAll = best
                    averageOfAll += average
            print("Best of all: " + str(bestOfAll))
            print("Average of all: " + str(averageOfAll / numberOfSolutions))
    elif type == 'b':
        print('1. Read from file:')
        print('2. Read from local data')
        x = input()
        if x == '1':
            file = input('Choose file: \n 1. rucsac-20.txt \n 2. rucsac-200.txt \n')
            nameOfFile = ''
            if file == '1':
                nameOfFile = 'rucsac-20.txt'
            else:
                nameOfFile = 'rucsac-200.txt'

            numberOfSolutions = int(input('Enter number of solutions to be generated: \n'))
            bestOfAll = 9999999  # get from file
            averageOfAll = 0
            for l in range(0, 9):
                f = open(nameOfFile)
                # Read first line of .txt file -> number of objects
                fileNumberOfObjects = [int(x) for x in next(f).split()][0]
                fileWeights = []
                fileValues = []

                # Read weights and values from file
                for line in f:
                    object = [int(x) for x in line.split()]
                    if (len(object) < 3):
                        break
                    fileWeights.append(object[1])
                    fileValues.append(object[2])
                # Read last line of file -> backpack capacity
                for line in f:
                    pass
                fileBackpackCapacity = int(line)
                average = 0
                for m in range(0, numberOfSolutions):
                    solution, quality = [], 0
                    try:
                        solution, quality = randomHillClimbing(fileWeights, fileValues, fileBackpackCapacity, 100)
                    except:
                        continue
                    print(str(m) + '.' + str(solution) + " Quality: " + str(quality))
                    average += quality
                    if quality < bestOfAll:
                        bestOfAll = quality
                average = average / numberOfSolutions
                averageOfAll += average
                f.close()
            print("Best of all: " + str(bestOfAll))
            print("Average of all: " + str(averageOfAll / numberOfSolutions))
        elif x == '2':
            numberOfSolutions = int(input('Enter number of solutions to be generated: \n'))
            bestOfAll = 999999999
            averageOfAll = 0
            # simulare 10 rulari
            for l in range(0, 9):
                average = 0
                for m in range(0, numberOfSolutions):
                    solution, quality = [], 0
                    try:
                        solution, quality = randomHillClimbing(weights, values, backpackCapacity, 1000)
                    except:
                        continue
                    print(str(m) + '.' + str(solution) + " Quality: " + str(quality))
                    average += quality
                    if quality < bestOfAll:
                        bestOfAll = quality
                average = average / numberOfSolutions
                averageOfAll += average
            print("Best of all: " + str(bestOfAll))
            print("Average of all: " + str(averageOfAll / numberOfSolutions))


start()

