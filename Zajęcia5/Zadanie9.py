def apply_function_to_tuples(tuples, func):
    return [func(*t) for t in tuples]

def sum_elements(a, b):
    return a + b

tuples = [(1, 2), (3, 4), (5, 6)]
print(apply_function_to_tuples(tuples, sum_elements))
