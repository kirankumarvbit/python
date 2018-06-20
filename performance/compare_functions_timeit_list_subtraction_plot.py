# Subtract items in a list backwards. The subtraction should go like this: 
# index 1 - index 0, index 2 - index 1, and so on and so forth.
# refer https://stackoverflow.com/questions/50940549/how-to-subtract-backwards-in-a-list-in-python-3#50940755

# import these libraries
import operator
from itertools import islice
from timeit import timeit
from itertools import chain
import tkinter
import pandas as pd
import matplotlib.pyplot as plt

# function 1 
def fun1(l):
    return [map(operator.sub, islice(l, 1, None), l)]

# function 2
def fun2(l):
    return [i - j for i, j in zip(l[1:], l)]

# function 3
def fun3(l):
    for i in range(len(l)-1,1,-1):
        l[i] = l[i]-l[i-1]
    return l[i]

# function 4
def fun4(l):
    return [l[i+1]- l[i] for i in range(len(l)-1)]

# function 5
def fun5(l):
    return [(l[i+1] - l[i]) for i in range(len(l)-1)]

# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2', 'fun3', 'fun4', 'fun5',],
       columns=[10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],
       dtype=float
)

# each function to be looped over the mul.factors
# timeit is used and output to dataframe
for f in res.index: 
    for c in res.columns:
        l = [1,2,3,4,5,6,7,8,9,10] * c
        stmt = '{}(l)'.format(f)       # f(l)
        setp = 'from __main__ import l, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=50)

# using matplotlib to plot 
ax = res.div(res.min()).T.plot(loglog=True) 
ax.set_xlabel("N"); 
ax.set_ylabel("time (relative)");

plt.show()
