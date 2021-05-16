"""
Created on Sat May  8 09:59:01 2021

@author: Innan Nouhaila
"""

"""
relu
~~~~
Plots a graph of the squashing function used by a rectified linear
unit."""

import numpy as np
import matplotlib.pyplot as plt

z = np.arange(-2, 2, .1)
zero = np.zeros(len(z))
y = np.max([zero, z], axis=0)

plt.plot(z, y)
plt.ylim([-1.0, 3.0])
plt.xlim([-2.0, 2.0])
plt.grid(True)
plt.xlabel('x')

plt.title('Rectified linear unit function')
plt.ylabel('ReLU(x)')
plt.text(-1.75, 2.5, r'$ReLU(x)=max(x,0)$', fontsize=15)
plt.show()
