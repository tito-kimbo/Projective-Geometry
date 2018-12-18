# -*- coding: utf-8 -*-
# Homographies
from sage.all import matrix,vector

from applications import *
from basic.subspaces import *
    

class homography(application):
    
    def __init__(self, m):
        application.__init__(self,m)
        if self.matrix.ncols() != self.matrix.nrows() or self.matrix.rank() != self.matrix.ncols():
            raise ValueError("The homography must be bijective.")
            
class involution(homography):
    
    def __init__(self, m):
        homography.__init__(self,m)
        if sum([self.matrix[i][i] for i in range(self.matrix.nrows())]) != 0:
            raise ValueError("Non-zero trace: The given homography is not an involution.")