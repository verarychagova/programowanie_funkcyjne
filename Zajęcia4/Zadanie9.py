def zip_with_index(lst):
    return list(enumerate(lst))

items = ['apple', 'banana', 'cherry']

result = zip_with_index(items)

print(result)