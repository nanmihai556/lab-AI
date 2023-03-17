import random

from functions.getBestAndAverageSolution import getBestAndAverageSolution
from functions.solutionIsValid import solutionIsValid


# Function that generates K random solutions
# Parameters:   k - number of generated solutions
#               weights - weights array
#               values - values array
#               solutionLength - number of objects used for the problem
#               backpackCapacity - backpack capacity
def generateRandomSolutions(k, weights, values, solutionLength, backpackCapacity):

    allSolutions = []
    for i in range(0, k):
        solution = []

        # Generate random values in each solution
        for j in range(0, solutionLength):
            solution.append(random.randint(0, 1))
        allSolutions.append(solution)

        # Verify if the solution is valid
        print(str(i) + '.' + solutionIsValid(weights, values, solution, backpackCapacity))

    # Get the best and average solution
    bestSolution, averageSolution = getBestAndAverageSolution(allSolutions, weights, values, backpackCapacity)
    print("Backpack capacity " + str(backpackCapacity))
    print('Best solution of this run: ' + str(backpackCapacity - bestSolution[2]))
    return [backpackCapacity - bestSolution[2], averageSolution]
