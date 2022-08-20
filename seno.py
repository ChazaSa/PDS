#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:23:15 2022

@author: chaz
"""

import numpy as np


import matplotlib.pyplot as plt 


def mi_funcion(Vm=0, A=1,frec=10, fase=np.pi/2, N=200, frecADC=250):
    
    ts = 1/frecADC
    tt = np.linspace(0,(N-1)*ts, N)
    ff = Vm + A*np.sin(2*np.pi*frec*tt + fase)
    plt.figure(1)
    plt.plot(tt, ff, 'ro')
    plt.title('senoidal')
    plt.xlabel('tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.show()    



    
mi_funcion(50,5,10,np.pi,100,500)



