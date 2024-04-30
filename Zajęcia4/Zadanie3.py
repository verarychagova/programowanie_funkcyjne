def recursive_sum(numbers):
    total = 0
    for element in numbers:
        if isinstance(element, list):
            total += recursive_sum(element)
        else:
            total += element

    return total

print(recursive_sum([1, [2, 3], [4, [5, 6]]]))

