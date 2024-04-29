def filter_even_numbers(input_tuple):
    even_numbers = tuple(n for n in input_tuple if n % 2 == 0)
    return even_numbers


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
filtered_tuple = filter_even_numbers(my_tuple)
print(filtered_tuple)