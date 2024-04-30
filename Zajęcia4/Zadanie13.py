def split_list(lst, chunk_size):
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

print(split_list([1, 2, 3, 4, 5, 6, 7, 8], 3))
