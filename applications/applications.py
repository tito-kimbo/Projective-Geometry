# -*- coding: utf-8 -*-
# Projective applications
from sage.all import matrix,vector
from basic.subspaces import *
    
"""Represents a projective application"""
class application:
    
    def __init__(self, m):
        self.matrix = matrix(m)
        if min(self.matrix.ncols(), self.matrix.nrows()) == 0:
            raise ValueError("The application must be defined over a non-empty space.")
        aux = [[self.matrix.T[i][j] for j in range(self.matrix.ncols())] for i in range(self.matrix.nrows())]
        aux.append([0 for i in range(len(aux[0]))])
        self.center = subspace(matrix(aux).T)
    
    """Given an application f we can call f(x) over a vector or an array of adequate size."""
    def __call__(self,x):
        return self.matrix*vector(x)