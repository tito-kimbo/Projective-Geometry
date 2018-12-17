# -*- coding: utf-8 -*-
# cuadrics
from sage.all import matrix,var,vector,solve,det

"""Returns whether matrix m is symmetric (assuming it is square)"""
def symmetric(m):
    for i in range(m.nrows()):
        for j in range(i, m.ncols()):
            if m[i][j] != m[j][i]:
                return False
    return True
                
"""Class representing a cuadric through its matrix."""
class cuadric:
    
    def __init__(self, m):
        self.matrix = matrix(m)
        self.dim = self.matrix.nrows()
        if(self.dim != self.matrix.ncols() or not symmetric(self.matrix)):
            raise ValueError("Matrix must be square and symmetric.")
        self.det = det(self.matrix)
    
    #This function is considerably slow and should only be used to probe values
    def points(self):
        vars = [var('x' + str(i)) for i in range(self.dim)]
        x = vector(vars)
        return solve(x*self.matrix*x==0, vars)
    
    def isDegenerate(self):
        return det(self.matrix) == 0
        
    def explicit_equation(self):
        vars = [var('x' + str(i)) for i in range(self.matrix.ncols())]
        eq = vector(vars)*self.matrix*vector(vars)==0
        return eq.full_simplify()