import itertools


def combi(list1):
    res = []
    combinations = list(itertools.combinations(list1, 2))
    for c in combinations:
        res.append(c)
    return res


list2 = ['a', 'b', 'c', 'd']
print(combi(list2))
