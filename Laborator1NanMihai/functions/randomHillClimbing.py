import random

from functions.fitnessFunc import fitnessFunc
from functions.neighboursFunc import randomNeighboursFunc


def randomHillClimbing(weights, values, backpackCapacity, iterations=1000):
    # Start with a random solution
    currentSolution = [random.randint(0, 1) for _ in range(len(weights))]
    bestSolution = currentSolution
    bestFitness = fitnessFunc(currentSolution, weights, values, backpackCapacity)

    for i in range(iterations):
        randomNeighbour = randomNeighboursFunc(currentSolution)

        randomNeighbourFitness = fitnessFunc(randomNeighbour, weights, values, backpackCapacity)

        if randomNeighbourFitness > bestFitness:
            currentSolution = randomNeighbour
            bestSolution = currentSolution
            bestFitness = randomNeighbourFitness

    # Return the best solution found after the specified number of iterations
    totalWeight = 0
    for id, weight in enumerate(weights):
        totalWeight += weight * bestSolution[id]
    if backpackCapacity - totalWeight >= 0:
        return bestSolution, backpackCapacity - totalWeight
