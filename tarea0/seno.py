#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:23:15 2022

@author: chaz
"""

import numpy as np


import matplotlib.pyplot as plt 


def sen(N, FADC, Vm=0, A=1,frec=1, fase=0):
    
    ts = 1/FADC
    tt = np.linspace(0,(N-1)*ts, N)
    ff = Vm + A*np.sin(2*np.pi*frec*tt + fase)
    return tt, ff

    
tt,ff = sen(Vm=50, A=5,frec=1, fase=np.pi/2, N=1000, FADC=1000)

plt.figure()
plt.plot(tt, ff, 'ro')


