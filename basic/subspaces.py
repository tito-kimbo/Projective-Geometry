# -*- coding: utf-8 -*-
from sage.all import matrix,var,solve

class subspace:
    
    # Constraints are given as a matrix of the form (w|b)
    # Where w are the coefficients and b the independent term
    def __init__(self, constraints):
        self.constraints = constraints
    
    def getMatrix(self):
        return matrix(self.constraints)
    

# Calculate equations -> returns the equations and the variables associated
def equations(subspace_matrix, variables):
    #Probably can apply list comprehension here
    last = subspace_matrix.ncols()-1
    equations = []
    for i in range(subspace_matrix.nrows()):
        eq = 0
        for j in range(last):
            eq += subspace_matrix[i][j]*variables[j]
        equations.append(eq == subspace_matrix[i][last])
    return equations
        
# Intersect
def intersect(subspaces):
    matrices = [s.getMatrix() for s in subspaces]
    vars = [var('x'+str(i)) for i in range(matrices[0].ncols()-1)]
    eqs = []
    for s in subspaces:
        eqs.append(equations(s.getMatrix(),vars))
    return solve(eqs, vars)