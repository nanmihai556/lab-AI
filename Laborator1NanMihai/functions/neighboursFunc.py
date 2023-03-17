# Define the neighbours function
import random


def randomNeighboursFunc(solution):
    neighbours = []
    for i in range(len(solution)):
        neighbor = list(solution)
        neighbor[i] = 1 - neighbor[i]  # flip one bit
        neighbours.append(neighbor)  # e.g. [1,0,1,0] -> [0,1,0,1]

    return neighbours[random.randint(0, len(neighbours))]
