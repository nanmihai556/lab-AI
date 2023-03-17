# Define the fitness function
def fitnessFunc(solution, weights, values, backpackCapacity):
    total_weight = 0
    total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
            if total_weight > backpackCapacity:
                return 0
    return total_value
