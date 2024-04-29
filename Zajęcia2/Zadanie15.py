def add(x):
    def inner_add(y):
        return x + y
    return inner_add

res = add(1)(2)
print(res)
