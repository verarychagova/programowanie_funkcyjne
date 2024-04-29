import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res

    return wrapper


@timeit
def func():
    summ = 0
    for i in range(100000000):
        summ += 1
    return summ


result = func()
print(result)