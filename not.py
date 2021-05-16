"""
Created on Sat May  8 23:35:27 2021

@author: INNAN Nouhaila
"""

import numpy as np

def unit_step(v):
	""" Heavyside Step function. v must be a scalar """
	if v >= 0:
		return 1
	else:
		return 0
	
def perceptron(x, w, b):
    """ Function implemented by a perceptron with 
		weight vector w and bias b """
    v = np.dot(w, x) + b
    y = unit_step(v)
    return y

def NOT_percep(x):
	return perceptron(x, w=-1, b=0.5)

print("NOT(0) = {}".format(NOT_percep(0)))
print("NOT(1) = {}".format(NOT_percep(1)))
