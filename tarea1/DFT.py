#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:22:43 2022

@author: chaz
"""

from seno import sen 

import numpy as np


import matplotlib.pyplot as plt 

def mi_DFT(xx):
    N = len(xx)
    K = N//2
    XX = np.empty(K, dtype=complex)
    
    for k in range(K):
        
        XX[k]=0 
        
        for n in range(N-1):
            
            W = np.cos(2*np.pi*k*n/N) + 1j*np.sin(2*np.pi*k*n/N)
            XX[k]+= xx[n]*W 
            
        XX[k]= abs(XX[k])   
        
        
    fs = np.linspace(0,K-1,N//2)
    
    return fs, XX


tt, xx2 = sen(A=3,N=100, FADC=100, frec=2)
tt, xx3 = sen(N=100, FADC=100, frec=8)
tt, xx4 = sen(A=4,N=100, FADC=100, frec=16)
tt, xx5 = sen(N=100, FADC=100, frec=46)

xx= xx2 +xx3+xx4+xx5

fs, XX = mi_DFT(xx)

plt.figure()
plt.plot(fs, XX, 'bo')

sp= abs(np.fft.fft(xx))
freq = np.fft.fftfreq(tt.shape[-1])
plt.figure()
plt.plot(freq, sp, 'ro')
