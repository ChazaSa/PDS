#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:23:15 2022

@author: chaz
"""

import numpy as np


import matplotlib.pyplot as plt 


def mi_funcion(Vm, A,frec, fase, N, frecADC):
    
    ts = 1/frecADC
    tt = np.linspace(0,(N-1)*ts, N)
    ff = Vm + A*np.sin(2*np.pi*frec*tt + fase)
    return tt, ff

    
tt,ff = mi_funcion(Vm=50, A=5,frec=10, fase=np.pi/2, N=100, frecADC=500)
plt.figure()
plt.plot(tt, ff, 'ro')

