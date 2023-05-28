# Collections: Counter, namedtuple, orderedDict, defaultdict, deque
# Itertools: product, permutations, combinations, accumalate, groupby, and infinite itereations
from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
