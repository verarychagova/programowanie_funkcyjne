def add_two(number):
    return number + 2

def func_for_list(numbers, func):
    return [func(n) for n in numbers]

list_of_numbers = [1, 2, 3]
print(func_for_list(list_of_numbers, add_two))