def filter_even_numbers(list_of_numbers):
    return list(filter(lambda x: x % 2 == 0, list_of_numbers))


numbers_list = [1, 2, 3, 4, 5, 6, 7]
even_numbers = filter_even_numbers(numbers_list)
print(even_numbers)
