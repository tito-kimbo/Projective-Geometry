# -*- coding: utf-8 -*-
# Homographies
from sage.all import matrix

class homography:
    
    def __init__(self, m):
        self.matrix = matrix(m)