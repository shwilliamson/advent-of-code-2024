from itertools import product
from typing import Tuple


x = [0, 1, 2, 3]
for y in product(x, repeat=2):
    print(y)