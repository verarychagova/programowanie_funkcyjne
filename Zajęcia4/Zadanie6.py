def multiply_by_two(x):
    return x * 2

def map_nested(func, nested_list):
    result = []
    for el in nested_list:
        if isinstance(el, list):
            result.append(map_nested(func, el))
        else:
            result.append(func(el))

    return result


nested_list = [1, [2, 3, [4, 5]], 6]

mapped_result = map_nested(multiply_by_two, nested_list)

print(mapped_result)