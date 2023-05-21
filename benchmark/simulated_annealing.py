import random
import math
import csv
from objective_functions import *

search_space = range(-5, 6)

initial_temperature = 1000
min_temperature = 0.1
cooling_rate = 0.99
num_iterations = 10000


def generate_neighbor(solution, search_space):
    search_space_fraction = (len(search_space) - 1) * 0.1
    solution = solution.copy()
    for i in range(len(solution)):
        choice = int(random.choice((-search_space_fraction, search_space_fraction)))
        if solution[i] + choice in search_space:
            solution[i] += choice
        else:
            solution[i] -= choice

    return solution


def acceptance_probability(old_fitness, new_fitness, temperature):
    if new_fitness < old_fitness:
        return 1.1
    return math.exp((old_fitness - new_fitness) / temperature)


def simulated_annealing(objective_function, search_space, initial_temperature, cooling_rate, num_iterations,
                        dimensions):
    x = 0
    solution = [random.choice(search_space) for _ in range(dimensions)]
    best_solution = solution
    temperature = initial_temperature
    if objective_function == schwefel:
        search_space = range(-500, 501)

    while temperature > min_temperature:
        neighbours = [generate_neighbor(solution, search_space) for _ in range(11)]
        for neighbor in neighbours:
            current_fitness = objective_function(solution)
            neighbor_fitness = objective_function(neighbor)
            if acceptance_probability(current_fitness, neighbor_fitness, temperature) > random.random():
                solution = neighbor
            if objective_function(solution) < objective_function(best_solution):
                best_solution = solution
            x += 1

        temperature *= cooling_rate

    print(x)

    return best_solution, objective_function(best_solution)


if __name__ == "__main__":
    for i in range(30):
        print(simulated_annealing(first_dejong, search_space, initial_temperature, cooling_rate, num_iterations, 5))
    for i in range(30):
        print(simulated_annealing(first_dejong, search_space, initial_temperature, cooling_rate, num_iterations, 10))
    for i in range(30):
        print(simulated_annealing(second_dejong, search_space, initial_temperature, cooling_rate, num_iterations, 5))
    for i in range(30):
        print(simulated_annealing(second_dejong, search_space, initial_temperature, cooling_rate, num_iterations, 10))
    for i in range(30):
        print(simulated_annealing(schwefel, search_space, initial_temperature, cooling_rate, num_iterations, 5))
    for i in range(30):
        print(simulated_annealing(schwefel, search_space, initial_temperature, cooling_rate, num_iterations, 10))
