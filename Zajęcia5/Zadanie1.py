def sum_of_evens(numbers):
    return sum(x for x in numbers if x % 2 == 0)

print(sum_of_evens([1, 2, 3, 4, 5]))
