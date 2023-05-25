from knapsack import *
import matplotlib.pyplot as plt


def data_export():
    plt.figure()
    sa_all_best_prices=[]
    bf_all_best_prices=[]
    for i in range(30):
        generated_items = generate_items(20, 1, 50, 1, 50)

        bf_best_combination, bf_best_weight, bf_best_price = brute_force_solution(generated_items)

        sa_best_combination, sa_best_weight, sa_best_price, sa_best_prices = simulated_annealing_solution(generated_items)

        sa_all_best_prices.append(sa_best_prices)
        bf_all_best_prices.append(bf_best_price)

    sa_average_best_price = [sum(best_price) / len(best_price) for best_price in zip(*sa_all_best_prices)]
    bf_average_best_price = [sum(bf_all_best_prices) / len(bf_all_best_prices)]

    plt.plot(sa_average_best_price, linewidth=0.5)
    plt.axhline(y=bf_average_best_price, color='r', linestyle='--')
    plt.show()


if __name__ == "__main__":
    data_export()