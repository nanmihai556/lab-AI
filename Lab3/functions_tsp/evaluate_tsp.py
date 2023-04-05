# Evaluate a solution
from Lab2TabuSearch.distance import distance


def evaluate_tsp(solution, coords):
    total_distance = 0
    for i in range(len(solution)):
        total_distance += distance(coords[solution[i]], coords[solution[(i + 1) % len(solution)]])
    return 1 / total_distance
