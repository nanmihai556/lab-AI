import random


def generate_initial_solution(n, data):
    solution = list(range(1, n + 1))
    random.shuffle(solution)
    return solution
