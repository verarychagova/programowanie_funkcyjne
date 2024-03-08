def square(number):
    return number ** 2


def add(number):
    return number + 5


numbers_list = [2, 3, 4, 5]
res = list(map(square, map(add, numbers_list)))
print(res)
