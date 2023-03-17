# Function that verifies if a solutions is valid
# Parameters:   weightsArray - weights array
#               valuesArray - values array
#               solutionArray - solution array
#               backpackCapacity - backpack capacity

def solutionIsValid(weightsArray, valuesArray, solutionArray, backpackCapacity):
    totalWeight = 0
    totalValue = 0

    # Calculate the total value and total weight of the objects with respect to the solution
    for i in range(0, len(solutionArray)):
        totalValue += solutionArray[i] * valuesArray[i]
        totalWeight += solutionArray[i] * weightsArray[i]

    # Verify if the total weight doesn't exceed the backpack capacity(solution condition to be valid)
    result = totalWeight < backpackCapacity
    return 'Solution array ' + str(solutionArray) + '. Solution is ' + ('valid' if result else 'invalid')
