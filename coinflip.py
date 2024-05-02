#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:00:29 2024

@author: reggiehacker
"""

import numpy as np

x= int(input('What degree of flips do you want (IE 1 = 10, 2 = 100 etc.)?'))
deg = 10**x

rng = np.random.default_rng()

samples = rng.random(deg)

samples2 = (samples>0.5)

heads = sum(samples2)
tails = deg - heads

print(heads, 'heads')
print(tails, 'tails')



