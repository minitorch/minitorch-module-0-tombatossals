"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def id(x):
    return x

def neg(x):
    return -x

def lt(a,b):
    return 1.0 if a < b else 0.0

def eq(a,b):
    return 1.0 if a == b else 0.0

def inv(x):
    return 1.0 / x

def relu(x):
    return x if x > 0 else 0.0

def relu_back(x, d):
    return d if x > 0 else 0.0

def inv_back(x, d):
    return x

def log_back(x, d):
    return x

def max(a,b):
    return a if a > b else b

def exp(x):
    return math.exp(x)

def is_close(x,y):
    return 1.0 if abs(x-y) < 1e-2 else 0.0

def log(x):
    return math.log(x)

def sum(ls):
    return reduce(add, ls)

def reduce(fn: Callable[[float, float], float], ls: Iterable[float], initial: float = 0.0) -> float:
    acc = initial
    for x in ls:
        acc = fn(acc, x)
    return acc

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    return zipWith(add, ls1, ls2)

def negList(ls: Iterable[float]) -> Iterable[float]:
    return map(neg, ls)

def prod(ls: Iterable[float]) -> float:
    return reduce(mul, ls, 1.0)

def zipWith(fn: Callable[[float, float], float], ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    return [fn(x,y) for x,y in zip(ls1, ls2)]

# TODO: Implement for Task 0.3.

def distribute(fn: Callable[[float, float], float], ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    return [fn(x,y) for x in ls1 for y in ls2]

def sigmoid(x):
    if x >= 0:
        return 1.0 / (1.0 + exp(-x))
    else:
        return exp(x) / (1.0 + exp(x))

def sum_distribute(ls1, ls2):
    return distribute(add, ls1, ls2)