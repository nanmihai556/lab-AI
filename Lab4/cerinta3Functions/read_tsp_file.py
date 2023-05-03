import numpy as np


def read_tsp_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    city_coords = []
    for line in lines:
        if line.startswith("EOF"):
            break
        city_id, x, y = line.strip().split()
        city_coords.append([float(x), float(y)])

    num_cities = len(city_coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i == j:
                continue
            dist_matrix[i, j] = np.linalg.norm(np.array(city_coords[i]) - np.array(city_coords[j]))

    return dist_matrix
