# Collections: Counter, namedtuple, orderedDict, defaultdict, deque
# Itertools: product, permutations, combinations, accumalate, groupby, and infinite itereations
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))

