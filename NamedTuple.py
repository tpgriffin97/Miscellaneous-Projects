# Namedtuples()
import collections
from collections import namedtuple

Point = namedtuple('Point', 'x y z')

# Iterable arguments can be iterated through and separated using namedtuple
newP = Point(3, 4, 5)
print(newP)
