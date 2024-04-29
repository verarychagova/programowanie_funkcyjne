square = lambda x: x ** 2

numbers = [1, 2, 3, 4, 5, 6, 7]
squared = list(map(square, numbers))
print(squared)