# Subtract items in a list backwards. The subtraction should go like this: 
# index 1 - index 0, index 2 - index 1, and so on and so forth.

import operator
from itertools import islice

list_1 = [1,2,3,4,5,6,7,8,9,10]

desired_list = list(map(operator.sub, islice(list_1, 1, None), list_1))

>>> desired_list
[1, 1, 1, 1, 1, 1, 1, 1, 1]
