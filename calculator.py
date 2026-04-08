"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if b < 1 or a < 1:
        raise ValueError
    return math.log(b,a)# use math library/raise ValueError

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)# raise ValueError if a < 0
def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a # raise ZeroDivisionError if a == 0

def exp(a, b):
    return math.pow(a,b)