#!/usr/bin/env python
# calculate the roots of a second order polynomial
# this version is fully interactive

import math

# this function is taken from lec05
def solve_second(a, b, c):
    if a == 0.0 and b == 0.0 and c == 0.0:
        raise RuntimeError("Infinite number of solutions")

    if a == 0.0:
        raise RuntimeError("a cannot be zero")
        
    d = b*b - 4*a*c
    if d < 0.0:
        raise FloatingPointError("The roots are not real")

    r1 = (-b - math.sqrt(d))/(2*a)
    r2 = (-b + math.sqrt(d))/(2*a)

    return r1, r2


# main program
print("This script find the real roots of a second order polynomial: a*x**2 + b*x + c = 0")
# get a, b and c from the keyboard
a = ...
b = ...
c = ...

r1, r2 = solve_second(a, b, c)
# print the roots
...
