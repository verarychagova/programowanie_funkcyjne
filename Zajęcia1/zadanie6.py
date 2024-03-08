words_list = ["apple", "banana", "apricot"]

starts_with_a = list(filter(lambda word: word.startswith('a'), words_list))
print(starts_with_a)

numbers_list = [2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers_list))
print(squares)