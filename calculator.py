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

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if b < 1 or a < 1:
        raise ValueError
    return math.log(b,a)# use math library/raise ValueError

def exponent(a, b):
    return a**b

def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if a < 1 or b < 1:
        raise ValueError('A and B need to be greater than 0')
    math.log(b,a) # use math library + raise ValueError

def exp(a, b):
    math.pow(a,b)