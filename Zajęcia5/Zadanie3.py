def filter_even_values(d):
    return {key: value for key, value in d.items() if value % 2 == 0}

dict = {'x': 1, 'y': 2, 'z': 5}
print(filter_even_values(dict))