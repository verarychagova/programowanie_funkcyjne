def add(a):
    return a + 2


def apply_twice(function, value):
    first = function(value)
    second = function(first)
    return second


print(apply_twice(add, 2))
