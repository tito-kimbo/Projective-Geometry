# -*- coding: utf-8 -*-
# Homographies
from sage.all import matrix,vector

from applications import *
from basic.subspaces import *
    

class homography(application):
    
    def __init__(self, m):
        application.__init__(self,m)
        if self.matrix.rank() != min(self.matrix.ncols(), self.matrix.nrows()):
            raise ValueError("The homography must be injective.")