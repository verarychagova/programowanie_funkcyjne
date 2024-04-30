def custom_sort(lst, key_function):
    lst.sort(key=key_function)
    return lst

strings = ["banana", "apple", "cherry", "kiwi"]
custom_sort(strings, key_function=len)
print(strings)