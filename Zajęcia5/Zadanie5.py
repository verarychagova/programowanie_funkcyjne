def split_list_into_chunks(lst, chunk_size):
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    return chunks

print(split_list_into_chunks([1, 2, 3, 4, 5, 6, 7], 3))
