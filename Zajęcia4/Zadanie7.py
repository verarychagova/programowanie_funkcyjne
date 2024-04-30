def flatten_list(nested_list):
    flat_list = []
    for el in nested_list:
        if isinstance(el, list):
            flat_list.extend(flatten_list(el))
        else:
            flat_list.append(el)

    return flat_list

print(flatten_list([[], [1, 2, [], 3], [4, []], 5]))