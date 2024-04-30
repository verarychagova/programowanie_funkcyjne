def rotate_list(lst, k):
    if not lst:
        return lst

    n = len(lst)
    k = k % n

    rotated_list = lst[-k:] + lst[:-k]
    return rotated_list


print(rotate_list([1, 2, 3, 4, 5], 8))  