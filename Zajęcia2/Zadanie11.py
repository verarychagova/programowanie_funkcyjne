words = ["banana", "apple", "cherry", "kiwi"]


def sorted_words(strings):
    sorted_w = sorted(strings, key=lambda s: len(s))
    return sorted_w


sorted_list = sorted_words(words)
print(sorted_list)
