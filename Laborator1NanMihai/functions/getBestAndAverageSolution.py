import functools
import operator


# Function that calculates the best and average solution from a generate solution array
# Parameters:   allSolutions - solution array
#               values - values array
#               backpackCapacity - backpack capacity

def getBestAndAverageSolution(allSolutions, weights, values, backpackCapacity):
    precisionArray = []
    for index, solution in enumerate(allSolutions):
        solutionPrecision = 0

        # Calculate the total value of each individual solution and save it in an array, along with the solution nr.
        solutionWeight = 0
        for i in range(0, len(solution)):
            solutionPrecision += solution[i] * values[i]
            solutionWeight += solution[i] * weights[i]
        precisionArray.append([index, solutionPrecision, solutionWeight])

    # Sort solution values array by values
    precisionArray = sorted(precisionArray, key=lambda x: x[1], reverse=True)

    # Get first solution from sorted array(best one)
    bestSolutionWeightValue = precisionArray[0][2]

    # Calculate average solution
    averageSolution = backpackCapacity - bestSolutionWeightValue / len(allSolutions)
    for solution in precisionArray:
        if backpackCapacity - solution[2] >= 0:
            return solution, averageSolution
