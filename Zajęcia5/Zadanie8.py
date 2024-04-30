from collections import Counter


def most_frequent(lst):
    if not lst:
        return None

    counter = Counter(lst)
    most_common = counter.most_common(1)

    return most_common[0][0] if most_common else None
