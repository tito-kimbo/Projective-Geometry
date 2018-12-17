# -*- coding: utf-8 -*-
# cuadrics
from sage.all import matrix,var,vector,solve

class cuadric:
    
    def __init__(self, m):
        self.matrix = matrix(m)
        self.dim = self.matrix.nrows()
    
    #This function is considerably slow and should only be used to probe values
    def points(self):
        vars = [var('x' + str(i)) for i in range(self.dim)]
        x = vector(vars)
        return solve(x*self.matrix*x==0, vars)
        