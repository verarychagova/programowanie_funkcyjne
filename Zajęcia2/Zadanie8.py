from functools import reduce


def sum_of_numbers(numbers_list):
    res = reduce(lambda a, b: a + b, numbers_list)
    return res

numbers = [1, 2, 3, 4, 6, 1, 3]

print(sum_of_numbers(numbers))
