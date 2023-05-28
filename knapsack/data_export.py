from knapsack import *
import matplotlib.pyplot as plt
import os

folder = "graphs"

if not os.path.exists(folder):
    os.makedirs(folder)


def data_export():
    plt.figure()
    sa_all_best_prices = []
    bf_all_best_prices = []
    sa_final_best_prices = []
    number_of_repetitions = 30
    for i in range(number_of_repetitions):
        generated_items = generate_items(20, 1, 50, 1, 50)

        bf_best_combination, bf_best_weight, bf_best_price = brute_force_solution(generated_items)

        sa_best_combination, sa_best_weight, sa_best_price, sa_best_prices = simulated_annealing_solution(
            generated_items)

        sa_all_best_prices.append(sa_best_prices)
        bf_all_best_prices.append(bf_best_price)
        sa_final_best_prices.append(sa_best_price)

    sa_average_best_price = [sum(best_price) / len(best_price) for best_price in zip(*sa_all_best_prices)]
    bf_average_best_price = sum(bf_all_best_prices) / len(bf_all_best_prices)

    print(f'Average diff between BF and SA: {bf_average_best_price - (sum(sa_final_best_prices) / number_of_repetitions)}')
    print(f'Average value best of BF {bf_average_best_price}')

    plt.plot(sa_average_best_price, linewidth=0.5)
    plt.axhline(y=bf_average_best_price, color='r', linestyle='--')
    plt.savefig(os.path.join(folder, f'Convergence_of_SA_compared_to_BF.png'), dpi=500)
    plt.show()


if __name__ == "__main__":
    data_export()
