# -*- coding: utf-8 -*-
# Working with references
from sage.all import matrix

"""Basis points and unit point must be expressed in the old reference or
with respect to the canonic reference."""
class projective_reference:
    
    def __init__(self, basis, unit=None, canonic=True):
        self.dim = len(basis)
        self.basis = basis
        if unit is None:
            unit = sum(basis)
        else:
            pass #Calculate 
        self.unit = unit
        if(not self.isValid()):
            raise ValueError("The first ", self.dim, " points are not independent.\n") #Throw exception
        self.canonic = canonic
        
    def isValid(self): #Check for collinearity
        if self.dim<2:
            return True
        else:
            return matrix(basis).rank() == self.dim 
            
    def getMatrix(self):
        return matrix([x for x in self.basis]).T

"""Returns the matrix to change from the old reference to the new one.
If old_ref is None, then the canonic reference is considered as the old one."""
def refChangeMatrix(new_ref, old_ref=None):
    if old_ref is None:
        return new_ref.getMatrix().inverse()
    else:
        return old_ref.getMatrix()*new_ref.getMatrix().inverse()

# It is strongly recommended to use refChangeMatrix and then change the points by multiplying them
"""Changes a point from the old reference to the given new one."""
def changeRef(point, new_ref, old_ref=None):
    return refChangeMatrix(new_ref,old_ref)*point;