import numpy as np


# Define the Schwefel 1 function
def schwefel_1(x):
    return np.sum(np.square(np.cumsum(x)))
