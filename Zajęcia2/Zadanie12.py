from functools import partial

def multiply(x, y):
    return x * y

multiply_by_three = partial(multiply, y=3)

result = multiply_by_three(x=10)
print(result) 