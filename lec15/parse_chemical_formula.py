#!/usr/bin/env python

# parse chemical formulas to get a dictionary of (element,number of atoms)
# Davide Ceresoli <dceresoli@gmail.com>
# Programming for Chemistry 2025-2026 @ UniMI

import re
import math

elements = ['H', 'He', 
            'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 
            'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 
            'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
            'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
            

# split a formula into elements, numbers and parenthesis and return a list
# e.g. 'Ca(OH)2' => ['Ca', '(', 'O', 'H', ')', '2']
def _split_formula(formula):
    formula = formula.strip()
    return re.findall(r'([A-Z][a-z]?|\d+|\(|\))', formula)
    

# convert a formula into a list of lists
# e.g. 'Ca(OH)2' => [['Ca'], ['O', 'H'], ['O', 'H']]
def _formula_to_list(formula):
    mylist = []
    
    stack = []

    # split into a list, loop over the list
    for a in _split_formula(formula):
        
        # check if it is an element
        if a[0].isalpha():
            assert a in elements, f'{a} is not a valid element'
            mylist.append(a)
    
        # check if it is a number, duplicate the last element
        elif a[0].isdigit():
            last_element = mylist[-1]
            for i in range(int(a)-1):
                mylist.append(last_element)
                
        # check if it is a '(': save the list on the stack
        elif a == '(':
            stack.append(mylist)
            mylist = []
        
        # if ')' get the element on top of the stack and put it forward in the list 
        elif a == ')':
            mylist = [stack.pop(), mylist]
            
        else:
            raise RuntimeError('Invalid character:'+a)
            
    return mylist
    
    
# RECURSIVE function that "flattens" a list
# e.g.: [['Ca'], ['O', 'H'], ['O', 'H']] => ['Ca', 'O', 'O', 'H', 'H']
def _flatten_list(mylist):
    result = []
    
    for e in mylist:
        if type(e) == list:
            result.extend(_flatten_list(e))
        else:
            result.append(e)

    return result
    

# convert the flattened list and return a dictionary
# e.g. ['Ca', 'O', 'O', 'H', 'H'] => {'Ca':1, 'O':2, 'H': 2}
def _flatlist_to_dict(mylist):
    mydict = {}
    
    for element in mylist:
        mydict[element] = mylist.count(element)
            
    return mydict
    

# convert a chemical formula into a dictionary, optionally reducing to
# the number of formula units
def formula_to_dict(formula, reduce=False):
    mylist =  _formula_to_list(formula)
    flatlist = _flatten_list(mylist)
    mydict = _flatlist_to_dict(flatlist)
    
    if reduce:
        coeffs = list(mydict.values())
        gcd = math.gcd(*coeffs)
        
        for element in mydict.keys():
            mydict[element] = mydict[element] // gcd
    
    return mydict
    

# test the code
if __name__ == '__main__':

  formulas = ['NaCl', 'Ca(OH)2', 'Fe2Cd(H2O)3Na', 'Ca5Cl10', 'Si((CH2)3CH3)4']
  for f in formulas: 
      print(f, '=>', formula_to_dict(f))  

  print()
  
  for f in formulas:
      print(f, '=>', formula_to_dict(f, reduce=True))

