from collections import defaultdict


def merge_dicts(*dicts):
    merged_dict = defaultdict(int)

    for d in dicts:
        for key, value in d.items():
            merged_dict[key] += value

    return dict(merged_dict)
