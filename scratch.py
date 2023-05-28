# Collections: Counter, namedtuple, orderedDict, defaultdict, deque
# Itertools: product, permutations, combinations, accumalate, groupby, and infinite itereations
from itertools import groupby

persons = [{'name': 'Time', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 38}]

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))
