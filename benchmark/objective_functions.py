import math


def first_dejong(values):
    return sum(val ** 2 for val in values)


def second_dejong(x):
    return sum((100 * (x[i] ** 2 - x[i + 1]) ** 2 + (1 - x[i]) ** 2) for i in range(len(x) - 1))


def schwefel(x):
    return sum((value * -1) * math.sin(math.sqrt(abs(value))) for value in x)
