"""
Created on Sat May  8 10:08:26 2021

@author: Innan Nouhaila
"""

"""
tanh
~~~~
Plots a graph of the tanh function."""

import numpy as np
import matplotlib.pyplot as plt

z = np.arange(-5, 5, .1)
t = np.tanh(z)



plt.plot(z, t)

plt.grid(True)
plt.xlabel('x')
plt.title('tanh function')
plt.ylabel('tanh(x)')
plt.text(-4.5, 0.7, r'$tanh(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$', fontsize=15)

plt.show()
