from functools import reduce


def b_number(a, b):
    return a if a > b else b

numbers = [1, 2, 3, 4, 6, 1, 3]
b_n = reduce(b_number, numbers)
print(b_n)


def avg(numbers_list):
    sum = reduce(lambda a, b: a + b, numbers_list)
    return sum / len(numbers_list)

print(avg(numbers))