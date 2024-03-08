def say_hi():
    return "hi"


def say_hi_throw_this_function(function):
    res = function
    return res


r = say_hi_throw_this_function(say_hi())
print(r)