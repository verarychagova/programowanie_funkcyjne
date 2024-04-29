def infinite_integers():
    n = 0
    while True:
        yield n
        n += 1

even_numbers = (x for x in infinite_integers() if x % 2 == 0)

for _ in range(10):
    print(next(even_numbers))
