#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:21:30 2024

@author: reggiehacker
"""

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

#Define two seperates lists, one for each direction
vertical = rng.random(500) > 0.5
horizontal = rng.random(500) > 0.5

#Make them negative 1 or positive 1
vertical = 2*vertical - 1
horizontal = 2*horizontal - 1

#add lists together to find final coords
x = np.cumsum(horizontal)
y = np.cumsum(vertical)

#plot coords
plt.figure()
plt.plot(x,y)

plt.show()




