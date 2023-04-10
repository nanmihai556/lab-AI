import random


# Initialize a random solution
def initialize_random_solution(coords):
    solution = list(range(len(coords)))
    random.shuffle(solution)
    return solution
