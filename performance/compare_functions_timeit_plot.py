# compare functions
# performance checks
# timeit results 
# matlib plots
# refer https://stackoverflow.com/questions/50312305/what-is-the-best-way-to-interleave-two-lists
# input l=['a','b','c'] 
# output out_l = ['a','a_1','b','b_2','c','c_3']

# import these libraries
from timeit import timeit
from itertools import chain
import tkinter
import pandas as pd
import matplotlib.pyplot as plt

# function 1 
def fun1(l):
    return [ 
        l[int(i / 2)] + "_" + str(int(i / 2) + 1) if i % 2 != 0 else l[int(i/2)] 
        for i in range(0,2*len(l))
    ]

# function 2
def fun2(l):
    return [
        i for b in [[a, '{}_{}'.format(a, i)] 
        for i, a in enumerate(l, start=1)] 
        for i in b
    ]

# function 3
def fun3(l):
    return [j for i, a in enumerate(l, 1) for j in [a, '{}_{}'.format(a, i)]]

# function 4
def fun4(l):
    return [
        val 
        for pair in zip(l, [f'{k}_{j+1}' for j, k in enumerate(l)]) 
        for val in pair
    ]

# function 5
def fun5(l):
    def _cs1(l):
        for i, x in enumerate(l, 1):
            yield x
            yield f'{x}_{i}'

    return list(_cs1(l))

# function 6
def fun6(l):
    return list(chain.from_iterable(
        zip(l, [f'{x}_{i}' for i, x in enumerate(l, 1)]))
    )

# function 7
def fun7(l):
    out_l = [None] * (len(l) * 2)
    out_l[::2] = l
    out_l[1::2] = [f'{x}_{i}' for i, x in enumerate(l, 1)]
    return out_l

# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2', 'fun3', 'fun4', 'fun5', 'fun6', 'fun7'],
       columns=[10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],
       dtype=float
)

# each function to be looped over the mul.factors
# timeit is used and output to dataframe
for f in res.index: 
    for c in res.columns:
        l = ['a', 'b', 'c', 'd'] * c
        stmt = '{}(l)'.format(f)       # f(l)
        setp = 'from __main__ import l, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=50)

# using matplotlib to plot 
ax = res.div(res.min()).T.plot(loglog=True) 
ax.set_xlabel("N"); 
ax.set_ylabel("time (relative)");

plt.show()
