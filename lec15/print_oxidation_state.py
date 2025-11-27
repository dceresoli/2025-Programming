#!/usr/bin/env

# list all possible and plausible oxidation states of a compound
# Davide Ceresoli <dceresoli@gmail.com>
# Programming for Chemistry 2025-2026 @ UniMI

from itertools import product
from parse_chemical_formula import formula_to_dict


# most common oxidation states, this table is incomplete
valence = { 'H': [1],
            'Li': [1], 'Na': [1], 'K': [1], 'Rb': [1], 'Cs': [1],
            'Be': [2], 'Mg': [2], 'Ca': [2], 'Sr': [2], 'Ba': [2],
            'B': [3], 'Al': [3], 'Ga': [3], 'In': [3],
            'C': [4,2,-4], 'Si': [4,-4], 'Ge': [4,-4], 'Sn': [4,2],
            'N': [5,4,3,2,1,-3], 'P': [5,3,-3], 'As': [5,3,-3], 'Bi': [5,3],
            'O': [2,-2,-1,-0.5], 'S':[6,4,2,-2], 'Se': [6,4,2,-2],
            'F': [-1], 'Cl': [7,6,5,4,3,2,1,-1], 'Br': [5,3,1,-1],
            'Sc': [3], 'Ti': [4,3,2], 'V': [5,4,3,2], 'Cr': [6,5,4,3,2], 'Mn': [7,6,4,3,2],
            'Fe': [3,2], 'Co': [3,2], 'Ni': [2], 'Cu': [2,1], 'Zn': [2], 'Y': [3] }


# try every possible combination of oxidation states and print them
# when their sum is equal to charge of the ion
def print_oxidation_states(formula_dict, charge=0):
    found = False
    
    # make a list of oxidation states to try for each element
    tryoxi = []
    elements = list(formula_dict.keys())
    for element in elements:
        tryoxi.append(valence[element])

    # extract the coefficient for each element
    coeffs = list(formula_dict.values())
    
    # loop over all combinations of oxdation states
    for oxi in product(*tryoxi):
        total = 0
        for i in range(len(oxi)):
            total += oxi[i] * coeffs[i]
            
        if total == charge:
            # print this possibility
            for i in range(len(oxi)):
                element = elements[i]
                coeff = coeffs[i]
                oxidation = oxi[i]
                print(f'{coeff:+d}*{element}({oxidation:+g}) ', end='')
            print(f'==> {charge}')
            found = True
            
    if not found:
        print('no obvious oxidation states for this compound') 
    
    
if __name__ == '__main__':
    
    formulas = [('KOH',0), ('H3PO4',0), ('LiO2',0), ('SO4',-2), 
                ('H5O2',+1), ('BaTiO3',0), ('YTiO3',0), ('BaBiO3',0)]
                
    for (formula,charge) in formulas:
        print(f'[{formula}]^{charge:+d}:')
        print_oxidation_states(formula_to_dict(formula),charge)
        print()
        

