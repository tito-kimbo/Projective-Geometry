# -*- coding: utf-8 -*-
# Möbius transformations
from sage.all import matrix,var,vector

class mobius_transform:
    
    #The matrix is of the form
    #[a,b]
    #[c,d]
    def __init__(self, m):
        self.matrix = matrix(m)
        if(self.matrix.det() == 0):
            raise ValueError("Matrix must be non-singular.")
    
    """Transforms given theta through the mobius transform."""
    def transform_theta(self, theta):
        denom = self.matrix[1][0]*theta+self.matrix[1][1]
        if denom == 0:
            return 'NaN'
        return (self.matrix[0][0]*theta+self.matrix[0][1])/(denom)

    #Uses 2 variables t1 is theta and t2 is theta'
    #If the equation is of the form theta' = theta + k and t2=None then the returned equation
    #will be -k=0
    """Returns the explicit equation of the transform. If t2 is None, then returns
    the explicit equation needed to find fixed points."""
    def explicit_equation(self, t1, t2=None):        
        if t2 is None:
            t2 = t1
        return (self.matrix[1][0]*t1*t2+self.matrix[1][1]*t2-self.matrix[0][0]*t1-self.matrix[0][1]) == 0