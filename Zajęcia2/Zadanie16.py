def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def double(x):
    return x * 2

def increment(x):
    return x + 1


increment_then_double = compose(double, increment)


result = increment_then_double(3)
print(result)