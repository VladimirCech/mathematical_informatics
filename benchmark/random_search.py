import random
import math
import csv

global_search_space = range(-5, 6)
num_iterations = 10000


def first_dejong(values):
    return sum(val ** 2 for val in values)


def second_dejong(x):
    return sum((100 * (x[i] ** 2 - x[i + 1]) ** 2 + (1 - x[i]) ** 2) for i in range(len(x) - 1))


def schwefel(x):
    return sum((value * -1) * math.sin(math.sqrt(abs(value))) for value in x)


def random_search(objective_function, search_space, iterations, dimensions):
    best_solution = None
    best_fitness = float('inf')
    if objective_function == schwefel:
        search_space = range(-500, 501)

    for _ in range(iterations):
        solution = [random.choice(search_space) for _ in range(dimensions)]
        fitness = objective_function(solution)
        if fitness < best_fitness:
            best_solution = solution
            best_fitness = fitness

    return best_solution, best_fitness


if __name__ == '__main__':
    with open('random_search.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(["First DeJong"])
        for i in range(30):
            writer.writerow(random_search(first_dejong, global_search_space, num_iterations, 5))
        for i in range(30):
            writer.writerow(random_search(first_dejong, global_search_space, num_iterations, 10))

        writer.writerow(["Second DeJong"])
        for i in range(30):
            writer.writerow(random_search(second_dejong, global_search_space, num_iterations, 5))
        for i in range(30):
            writer.writerow(random_search(second_dejong, global_search_space, num_iterations, 10))

        writer.writerow(["Schwefel"])
        for i in range(30):
            writer.writerow(random_search(schwefel, global_search_space, num_iterations, 5))
        for i in range(30):
            writer.writerow(random_search(schwefel, global_search_space, num_iterations, 10))
        f.close()
