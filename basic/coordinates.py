# -*- coding: utf-8 -*-
# Coordinates
from sage.all import vector,Rational,var
from math import isnan

def __init__():
    pass

def vecAsFractions(vec):
    return [Rational(x) for x in vec]

"""Returnsh homogenized coordinates for given point."""
#NEED CHECK
def std_homogenize(vec, val=float('NaN')):
    aux = vec.list()
    z = var('z')
    if(math.isnan(val)):
        vec.append(z)
    else:
        vec.append(val)
    return vector(aux)

"""Returns dehomogenized coordinates for given point.

Assumes the last component is NOT 0 and vec is not empty"""
def std_dehomogenize(vec):
    aux = vec.list()
    prod = 1.0/aux[-1]
    aux.pop()
    return vector(aux)*prod
    
# Now for non-standard homogenization and dehomogenization

def gen_homogenize(vec, hyp):
    return

def gen_dehomogenize(vec, hyp):
    return