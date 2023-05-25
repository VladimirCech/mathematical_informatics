import random
import itertools

# random.seed('random')

number_of_items = 20
minimal_weight = 1
maximum_weight = 50

minimal_price = 1
maximum_price = 50


# def knapsack_objective_function(items, selection, capacity):
#     total_weight = sum(item[1] for item, is_selected in zip(items, selection) if is_selected)
#
#     if total_weight > capacity:
#         return 0
#     else:
#         return sum(item[1] for item, is_selected in zip(items, selection) if is_selected)


def generate_items(num_items, min_weight, max_weight, min_price, max_price):
    items = []
    for _ in range(num_items):
        weight = random.randint(min_weight, max_weight)
        price = random.randint(min_price, max_price)
        items.append((weight, price))

    print(items)

    return items


def brute_force_solution(items):
    best_weight = 0
    best_price = 0
    best_combination = []
    x = 0
    if len(items) <= 15:
        max_capacity = 100

    elif len(items) <= 30:
        max_capacity = 200

    else:
        max_capacity = 300

    for r in range(1, len(items) + 1):
        for combination in itertools.combinations(items, r):
            weight = sum(w for w, p in combination)
            price = sum(p for w, p in combination)
            x += 1
            if weight <= max_capacity and price > best_price:
                best_combination = combination
                best_weight = weight
                best_price = price
    print(x)

    return best_combination, best_weight, best_price


def simulated_annealing_solution(items):
    if len(items) <= 15:
        max_capacity = 100

    elif len(items) <= 30:
        max_capacity = 200

    else:
        max_capacity = 300

    best_weight = 0
    best_price = 0
    best_solution = []
    temperature = 10000
    min_temperature = 0.1
    cooling_rate = 0.99
    selection = [random.choice([True, False]) for _ in range(len(items))]
    best_price_values = []
    nt = 20
    x = 0

    while temperature > min_temperature:

        for _ in range(nt):
            total_weight = 0
            total_price = 0

            for i in range(len(items)):
                if selection[i]:
                    total_weight += items[i][0]
                    total_price += items[i][1]

            if total_weight <= max_capacity and total_price > best_price:
                best_solution = [item for count, item in enumerate(items) if selection[count]]
                best_weight = total_weight
                best_price = total_price

            for j in range(len(items)):
                if random.random() < 1 / len(items):
                    selection[j] = not selection[j]
            x += 1

            best_price_values.append(best_price)

        temperature *= cooling_rate

    print(x)

    return best_solution, best_weight, best_price, best_price_values


if __name__ == "__main__":
    generated_items = generate_items(number_of_items, minimal_weight, maximum_weight, minimal_price, maximum_price)

    print(brute_force_solution(generated_items))

    print(simulated_annealing_solution(generated_items))
