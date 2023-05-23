import math
import random
import matplotlib.pyplot as plt
from random_search import *
from simulated_annealing import *
import os

folder = "graphs"

if not os.path.exists(folder):
    os.makedirs(folder)


def data_export():
    objectives_and_dimensions = [(first_dejong, 5), (first_dejong, 10), (second_dejong, 5), (second_dejong, 10),
                                 (schwefel, 5), (schwefel, 10)]

    with open('random_search.csv', 'w') as f:
        pass

    with open('simulated_annealing.csv', 'w') as f:
        pass

    # Logic for random search data export

    for objective, dimension in objectives_and_dimensions:
        rs_all_iterations_values = []
        plt.figure()

        with open('random_search.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)

            for i in range(30):
                rs_best_solution, rs_fitness_values, rs_iterations_values = random_search(objective,
                                                                                          global_search_space,
                                                                                          num_iterations, dimension)

                rs_all_iterations_values.append(rs_iterations_values)

                writer.writerow([objective.__name__, dimension, rs_best_solution, rs_fitness_values])

            f.close()

        if objective == second_dejong and dimension == 10:
            plt.ylim(0, 20000)
        elif objective == second_dejong and dimension == 5:
            plt.ylim(0, 5000)

        plt.xlabel('Iteration')
        plt.ylabel('Fitness')
        plt.title(f'RS convergence {objective.__name__} D = {dimension}')
        plt.savefig(os.path.join(folder, f'RS_convergence_{objective.__name__}_D_{dimension}.png'), dpi=500)
        plt.show()

        plt.figure()

        if objective == second_dejong and dimension == 10:
            plt.ylim(0, 20000)
        elif objective == second_dejong and dimension == 5:
            plt.ylim(0, 5000)

        plt.xlabel('Iteration')
        plt.ylabel('Fitness')
        plt.title(f'RS average convergence {objective.__name__} D = {dimension}')
        rs_average_fitness_values = [sum(fitness) / len(fitness) for fitness in zip(*rs_all_iterations_values)]
        plt.plot(rs_average_fitness_values, linewidth=1)
        plt.savefig(os.path.join(folder, f'RS_average_convergence_{objective.__name__}_D_{dimension}.png'), dpi=500)
        plt.show()  # List of objective functions and dimensions

        # Logic for simulated annealing export

        sa_all_iterations_values = []
        plt.figure()

        with open('simulated_annealing.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)

            for i in range(30):
                sa_best_solution, sa_fitness_values, sa_iterations_values = simulated_annealing(objective, search_space,
                                                                                                initial_temperature,
                                                                                                cooling_rate, dimension)

                plt.plot(sa_iterations_values, linewidth=0.2)

                sa_all_iterations_values.append(sa_iterations_values)

                writer.writerow([objective.__name__, dimension, sa_best_solution, sa_fitness_values])

            f.close()

        if objective == second_dejong and dimension == 10:
            plt.ylim(0, 20000)
        elif objective == second_dejong and dimension == 5:
            plt.ylim(0, 5000)

        plt.xlabel('Iteration')
        plt.ylabel('Fitness')
        plt.title(f'SA convergence {objective.__name__} D = {dimension}')
        plt.savefig(os.path.join(folder, f'SA_convergence_{objective.__name__}_D_{dimension}.png'), dpi=500)
        plt.show()

        plt.figure()

        if objective == second_dejong and dimension == 10:
            plt.ylim(0, 20000)
        elif objective == second_dejong and dimension == 5:
            plt.ylim(0, 5000)

        plt.xlabel('Iteration')
        plt.ylabel('Fitness')
        plt.title(f'SA average convergence {objective.__name__} D = {dimension}')
        sa_average_fitness_values = [sum(fitness) / len(fitness) for fitness in zip(*sa_all_iterations_values)]
        plt.plot(sa_average_fitness_values, linewidth=1)
        plt.savefig(os.path.join(folder, f'SA_average_convergence_{objective.__name__}_D_{dimension}.png'), dpi=500)
        plt.show()

        plt.figure()

        if objective == second_dejong and dimension == 10:
            plt.ylim(0, 20000)
        elif objective == second_dejong and dimension == 5:
            plt.ylim(0, 5000)

        # Logic for average comparison data export

        plt.xlabel('Iteration')
        plt.ylabel('Fitness')
        plt.title(f'Comparison between algorithms {objective.__name__} D = {dimension}')
        plt.plot(sa_average_fitness_values, linewidth=1, label='Simulated Annealing')
        plt.plot(rs_average_fitness_values, linewidth=1, label='Random Search')
        plt.legend()
        plt.savefig(os.path.join(folder, f'Comparison_convergence_{objective.__name__}_D_{dimension}.png'), dpi=500)
        plt.show()


if __name__ == "__main__":
    data_export()
