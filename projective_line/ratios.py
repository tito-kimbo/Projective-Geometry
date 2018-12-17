# -*- coding: utf-8 -*-
# ratios
from math import isnan

"""Auxiliary division which accepts division by zero and by infinity."""
def divide(num, denom):
    if isnan(num) and isnan(denom):
        return 1.0
    elif denom == 0:
        return float('nan')
    elif isnan(denom):
        return 0.0
    else:
        return num/float(denom)
    

"""Calculates the cross ratio (or anharmonic ratio) of 4 points.
Values of theta can be numeric or nan=float('nan') which is considered
infinity.
"""
def cross_ratio(theta0, theta1, theta2, theta3):
    # WE NEED TO FIRST SIMPLIFY POSSIBLE DIVISION BY 0
    # AND NaN (infinity) values
    num1 = theta0-theta2
    num2 = theta1-theta2
    denom1 = theta0-theta3
    denom2 = theta1-theta3
    
    #First come simplifications
    if isnan(num1) and isnan(num2):
        num1 = 1 
        num2 = 1
    if isnan(denom1) and isnan(denom2):
        denom1 = 1
        denom2 = 1
    
    #print(num1, "/", denom1, " : ",  num2, "/", denom2)
    #Then we calculate numerator and denominator
    finalNum = divide(num1,denom1)
    finalDen = divide(num2,denom2)
    
    return divide(finalNum,finalDen)

"""Calculates the division ratio of 3 points."""
def div_ratio3(theta0, theta1, theta2):
    return divide((theta1-theta0),(theta2-theta1))