#!/usr/bin/env python
# calculate the roots of a second order polynomial
# this version is a web application


import streamlit as st
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


st.title("🎈 Find the roots or a second order polynomial 🎈")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

a = st.number_input('Enter a:', value=1.0, step=1.0)
b = st.number_input('Enter b:', value=7.0, step=1.0)
c = st.number_input('Enter c:', value=-3.0, step=1.0)

try:
    r1, r2 = solve_second(a, b, c)
except:
    st.write("There was an error computing the root! Maybe they are complex.")
else:
    st.write(f"The roots are: {r1} and {r2}")

