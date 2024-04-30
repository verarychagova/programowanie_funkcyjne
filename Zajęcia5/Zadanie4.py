def power_function(exponent):
    def inner(base):
        return base ** exponent
    return inner

square = power_function(2)

print((square(5)))