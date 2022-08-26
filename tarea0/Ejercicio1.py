#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 21:38:22 2022

@author: chaz
"""

import matplotlib.pyplot as plt 

from seno import sen

tt, ff = sen(50,5,251,0,1000,1000)
plt.figure()
plt.plot(tt, ff, 'b.')

