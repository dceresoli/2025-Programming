#!/usr/bin/env python
# calculate the roots of a second order polynomial
# this version is a web application


import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
from threading import RLock
_lock = RLock()

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


# plot parabola
def plot_parabola(a, b, c):
    x = np.linspace(-10, 10, 200)
    p = a*x*x + b*x + c

    fig = plt.figure()
    plt.plot(x, p)
    plt.axhline(0, color='black', linewidth=0.5)    
    plt.axvline(0, color='black', linewidth=0.5)    
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    return fig


# main program
st.set_page_config(layout="wide") # Optional: Use wide layout for better viewing
st.title("🎈 Find the roots or a second order polynomial 🎈")

col1, col2 = st.columns(2)

with col1: 
    st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")
    a = st.number_input('Enter a:', value=1.0, step=1.0)
    b = st.number_input('Enter b:', value=7.0, step=1.0)
    c = st.number_input('Enter c:', value=-3.0, step=1.0)

with col2:
    try:
        r1, r2 = solve_second(a, b, c)
    except:
        st.write("There was an error computing the root! Maybe they are complex.")
    else:
        st.write(f"The roots are: {r1} and {r2}")
        with _lock:
    	    fig = plot_parabola(a, b, c)
    	    st.pyplot(fig, clear_figure=True)

