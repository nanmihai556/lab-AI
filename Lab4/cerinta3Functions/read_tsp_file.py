import numpy as np
from Lab2TabuSearch.read_data import read_data


def read_tsp_file(file_path):
    data = read_data(file_path)
    n = len(data)

    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.linalg.norm(np.array(data[i]) - np.array(data[j]))
            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist

    return dist_matrix
