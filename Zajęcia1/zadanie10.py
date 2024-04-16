def fib(number):
    a = 0
    b = 1
    c = 0
    for i in range(number):
        print (c)
        c = a + b
        a = b
        b = c



fib(10)


def read_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.rstrip('\n')

