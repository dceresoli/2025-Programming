#!/usr/bin/env python
# calculate the roots of a second order polynomial
# this version gets the coefficients from the CLI

import math
import sys

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
# check that len(sys.argv) is 4 otherwise print an error, then sys.exit(1)
...
...
...

# get a, b and c from sys.argv[] list
a = ...
b = ...
c = ...

r1, r2 = solve_second(a, b, c)
print(r1, r2)
