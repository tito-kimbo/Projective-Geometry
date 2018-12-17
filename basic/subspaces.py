# -*- coding: utf-8 -*-
from sage.all import matrix,var,solve

"""Class representing a subspace (whether vectorial or projective)"""
class subspace:
    
    # Constraints are given as a matrix of the form (w|b)
    # Where w are the coefficients and b the independent term
    def __init__(self, constraints):
        self.constraints = matrix(constraints)
        if self.constraints.nrows() == 0:
            raise ValueError("A subspace must have restrictions.")
        self.parent_dimension = constraints.ncols()-1
    

# Calculate equations -> returns the equations and the variables associated
def equations(subspace, variables=None):
    #Probably can apply list comprehension here
    subspace_matrix = subspace.constraints
    last = subspace_matrix.ncols()-1
    equations = []
    if variables is None:
        variables = [var('x'+str(i)) for i in range(last)]
    for i in range(subspace_matrix.nrows()):
        eq = 0
        for j in range(last):
            eq += subspace_matrix[i][j]*variables[j]
        equations.append(eq == subspace_matrix[i][last])
    return equations
        
# Intersect
def intersect(subspaces):
    if len(subspaces) == 0:
        raise ValueError("There must be subspaces to intersect.")
    #If parent dimension is different it should be treated
    vars = [var('x'+str(i)) for i in range(matrices[0].ncols()-1)]
    eqs = []
    for s in subspaces:
        eqs.append(equations(s,vars))
    return solve(eqs, vars)