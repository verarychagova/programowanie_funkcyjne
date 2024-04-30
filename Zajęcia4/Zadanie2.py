def filter_long_words(strings):
    if not strings:
        return []
    avg_length = sum(len(string) for string in strings) / len(strings)

    long_words = [string for string in strings if len(string) >= avg_length]
    return long_words

print(filter_long_words(["hello", "world", "python", "is", "great"]))