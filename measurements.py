#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:36:33 2024

@author: reggiehacker
"""
#import library
import numpy as np

#define "Taxi" function
def line_distance(A,B = (0,0), metric = "Straightline"):
    
    '''Sample function for computing
        x = ...
        y = ...
    Returns...
    '''
    #Define if you want the function to calculate straight line or euclidean
    if metric == "Straightline":
        line_dist = abs(A[0]-B[0]) + abs(A[1]-B[1])
    else:
        line_dist = np.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
    
    return line_dist






