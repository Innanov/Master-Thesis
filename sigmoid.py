"""
Created on Tue May 11 16:42:42 2021

@author: INNAN Nouhaila
"""

import math

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
plt.grid()


plt.xlabel('X')

plt.ylabel('Sigmoid(x)')
plt.text(-10, 0.89, r'$sigmoid(x)=\frac{1}{1+e^{-x}}$', fontsize=15)
plt.plot(x,sig,'b')
plt.show()
