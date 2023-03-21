import random


def tabu_search(weights, values, capacity, max_iter, tabu_size, num_solutions):
    solutions = []
    for _ in range(num_solutions):
        n = len(weights)
        current_solution = [random.randint(0, 1) for _ in range(n)]
        best_solution = current_solution
        best_solution_value = 0
        tabu_list = [set() for _ in range(n)]

        for i in range(max_iter):
            # Generate a list of neighboring solutions
            neighbors = []
            for j in range(n):
                if current_solution[j] == 0 and j not in tabu_list[j]:
                    neighbor = current_solution.copy()
                    neighbor[j] = 1
                    neighbors.append(neighbor)
                elif current_solution[j] == 1:
                    neighbor = current_solution.copy()
                    neighbor[j] = 0
                    neighbors.append(neighbor)

            # Evaluate the quality of each neighboring solution
            neighbor_values = [sum([values[j] for j in range(n) if neighbors[k][j] == 1]) for k in
                               range(len(neighbors))]
            neighbor_weights = [sum([weights[j] for j in range(n) if neighbors[k][j] == 1]) for k in
                                range(len(neighbors))]

            # Choose the best neighbor that does not violate the tabu rules
            # -infinity
            best_neighbor_value = -float('inf')
            best_neighbor_index = None
            for k in range(len(neighbors)):
                if neighbor_weights[k] <= capacity and neighbor_values[k] > best_neighbor_value and k not in tabu_list:
                    best_neighbor_value = neighbor_values[k]
                    best_neighbor_index = k

            if best_neighbor_index is not None:
                # Move to the best neighbor
                current_solution = neighbors[best_neighbor_index]
                if neighbor_values[best_neighbor_index] > best_solution_value:
                    best_solution = current_solution
                    best_solution_value = neighbor_values[best_neighbor_index]

                # Update the tabu list
                tabu_list.pop(0)
                tabu_list.append(set([j for j in range(n) if neighbors[best_neighbor_index][j] != current_solution[j]]))

            else:
                # All neighbors violate the tabu rules, so choose a random one
                current_solution = random.choice(neighbors)

        solutions.append((best_solution, best_solution_value))

    # Return the best solution out of all generated solutions
    return max(solutions, key=lambda x: x[1])
