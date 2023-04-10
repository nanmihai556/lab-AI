import random


# Initialization of a random solution
def initialize(objects):
    solution = [random.randint(0, 1) for _ in range(len(objects))]
    return solution
