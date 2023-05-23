import random
import math
import csv
import matplotlib.pyplot as plt
from objective_functions import *

search_space = range(-5, 6)

initial_temperature = 10000
min_temperature = 1
cooling_rate = 0.99
num_iterations = 10000


def generate_neighbor(solution, search_space):
    search_space_fraction = (len(search_space) - 1) * 0.05
    solution = solution.copy()
    for i in range(len(solution)):
        choice = random.choice((-search_space_fraction, search_space_fraction))
        if solution[i] + choice in search_space:
            solution[i] += choice
        else:
            solution[i] -= choice

    return solution


def acceptance_probability(old_fitness, new_fitness, temperature):
    if new_fitness < old_fitness:
        return 1.1
    return math.exp((old_fitness - new_fitness) / temperature)


def simulated_annealing(objective_function, search_space, initial_temperature, cooling_rate, dimensions):
    if objective_function == schwefel:
        search_space = range(-500, 501)

    solution = [random.choice(search_space) for _ in range(dimensions)]
    best_solution = solution
    temperature = initial_temperature
    fitness_values = []
    nt = 11

    while temperature > min_temperature:

        for i in range(nt):
            neighbor = generate_neighbor(solution, search_space)
            current_fitness = objective_function(solution)
            neighbor_fitness = objective_function(neighbor)

            if acceptance_probability(current_fitness, neighbor_fitness, temperature) > random.random():
                solution = neighbor

            if objective_function(solution) < objective_function(best_solution):
                best_solution = solution

            fitness_values.append(objective_function(best_solution))

        temperature *= cooling_rate

    return best_solution, objective_function(best_solution), fitness_values
