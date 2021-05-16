"""
Created on Sat May  8 15:19:25 2021

@author: INNAN Nouhaila
"""
import matplotlib.pyplot as plt
import numpy as np

def sgn(t):
    """Sign function"""
    return 1 * (t >= 0) - 1 * (t < 0)
t = np.linspace(-2, 2, 1000)

plt.figure()
plt.grid(True)
plt.xlabel('x')
plt.title('Sign Funtion')
plt.ylabel('sgn(x)')
  
plt.plot(t, sgn(t), '-b')
plt.ylim((-1.1, 1.1))

plt.show()
