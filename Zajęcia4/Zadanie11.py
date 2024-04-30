def find_max_min_diff(numbers):
    if not numbers:
        return None

    max_value = max(numbers)
    min_value = min(numbers)

    return max_value - min_value

print(find_max_min_diff([10, 15, 7, 22, 3]))