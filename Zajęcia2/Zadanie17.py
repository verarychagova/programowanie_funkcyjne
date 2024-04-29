from functools import partial

def add(a, b):
    return a + b

add_five = partial(add, 5)

print(add_five(5))