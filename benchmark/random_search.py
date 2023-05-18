import random

global_search_space = range(-5, 6)
num_iterations = 10000


def first_dejong(values):
    return sum(val ** 2 for val in values)


def second_dejong(values):
    pass


def random_search(objective_function, search_space, iterations, dimensions):
    best_solution = None
    best_fitness = float('inf')

    if objective_function is first_dejong:
        for _ in range(iterations):
            solution = [random.choice(search_space) for _ in range(dimensions)]

            fitness = objective_function(solution)

            if fitness < best_fitness:
                best_solution = solution
                best_fitness = fitness

    elif objective_function is second_dejong:
        for _ in range(iterations):
            solution = [random.uniform(search_space[i][0], search_space[i][1]) for i in range(len(search_space))]

            fitness = objective_function(solution)

            if fitness < best_fitness:
                best_solution = solution
                best_fitness = fitness

    return best_solution, best_fitness


if __name__ == '__main__':
    print(random_search(first_dejong, global_search_space, num_iterations, 5))
    print(random_search(first_dejong, global_search_space, num_iterations, 10))
