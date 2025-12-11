#!/usr/bin/env python

import streamlit as st
import math
import numpy as np

from balance_chemical_reaction import balance_chemical_reaction

# main program
st.set_page_config(layout="wide")       # wide layout for better viewing
st.title("Balance chemical reactions using linear algebra")

col1, col2 = st.columns([0.3,0.7])

with col1: 
    st.markdown('This webapp was code by the students of the **Programming for chemistry** course, academic year 2025/2026, at Università degli studi di Milano')
    st.image('logo_small.png') 

with col2:
    st.write('**Sample chemical reactions:**')
    st.write('''* CH4 +O2 = CO2 + H2O
* MnS + As2Cr10O35 + H2SO4 = HMnO4 + AsH3 + CrS3O12 + H2O
* NaNO3 + Zn + NaOH = Na2ZnO2 + NH3 + H2O
* MgSO4 + NaOH = Mg(OH)2 + Na2SO4
* K4Fe(CN)6 + KMnO4 + H2SO4 = KHSO4 + Fe2(SO4)3 + MnSO4 + HNO3 + CO2 + H2O''')

    st.write('**Don\'t try these reactions!**')
    st.write('''* H2O + NO2 = HNO3
* KNO3 + S + C = K2CO3 + K2SO4 + CO2 + N2
* P + HNO3 + H2O = H3PO4 + NO + NO2
* MnO2 + SO2 = MnS2O6 + MnSO4''')
    st.write()

    eq = st.text_input('Enter a chemical reaction:', value='')
    if eq != "":
        try:
            bal = balance_chemical_reaction(eq)
        except RuntimeError as e:
            st.write(f'Error: {e}')
        except Exception:
            st.write('Error in parsing or balancing the reaction!')
        else:
            st.write('The chemical reaction is:')
            st.write(bal)

