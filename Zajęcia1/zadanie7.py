def square(number):
    return number ** 2


def add(number):
    return number + 5

def add_function(number, *functions):
    for f in functions:
        number = f(number)
    return number

numbers_list = [2, 3, 4, 5]
res = [add_function(number, square, add) for number in numbers_list]
print(res)
