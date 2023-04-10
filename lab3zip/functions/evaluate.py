# Evaluation function of a solution
def evaluate(solution, weights, values, max_capacity):
    total_weight = 0
    total_value = 0
    for i in range(len(weights)):
        if solution[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
    if total_weight > max_capacity:
        total_value = 0
    return total_value
