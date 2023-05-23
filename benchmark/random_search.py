import random
import csv
import matplotlib.pyplot as plt
from objective_functions import *

global_search_space = range(-5, 6)
num_iterations = 10000


def random_search(objective_function, search_space, iterations, dimensions):
    best_solution = None
    best_fitness = float('inf')
    iterations_values = []
    if objective_function == schwefel:
        search_space = range(-500, 501)

    for _ in range(iterations):
        solution = [random.choice(search_space) for _ in range(dimensions)]
        fitness = objective_function(solution)
        if fitness < best_fitness:
            best_solution = solution
            best_fitness = fitness

        iterations_values.append(best_fitness)

    return best_solution, best_fitness, iterations_values


