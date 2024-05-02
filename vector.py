#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:25:23 2024

@author: reggiehacker
"""

import numpy as np

# =============================================================================
# def decompose(r, theta):
#     
#     '''
#     r: magnitude of vector
#     theta: angle/direction of vector in radians
#     
#     returns (r_x, r_y) components of r along x and y
#     '''
#     
#     r_y = r * np.sin(theta)
#     r_x = r * np.cos(theta)
#     
#     r_vector =(r_x, r_y)
#     
#     return r_vector
# =============================================================================


def rotate(vector, theta):
    '''
    

    Parameters
    ----------
    x : FLOAT
        x-component of vector
    y : FLOAT
        y-component of vector
    theta : FLOAT
        angle in radians

    Returns
    ------
    '''
    
    theta_radians = np.radians(theta)
    
    m1 = np.array([[np.cos(theta_radians), -(np.sin(theta_radians))], 
                  [np.cos(theta_radians), (np.sin(theta_radians))]]xxxxx`)
    
    rotated_vector = np.dot(m1, vector)
    
    return rotated_vector

vec = [1,0]
theta = 90

print(rotate(vec,theta))
    
    