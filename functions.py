import math
import numpy as np
import matplotlib.pyplot as plt
import random

def split_coordinates(a):
	"""
	Split a 2D Tensor of coordinate pairs into two vectors of x-coordinates and y-coordinates.
	This is helpful for plotting x and y pairs.

	Args:
		a (array_like): Array to be reshaped

	Returns:
		x, y: Returns two vectors of x and y coordinate points
	"""
	x, y = np.reshape(np.hsplit(a, 2), (2, -1))
	return x, y

def sin_generator(n, mu = 0, sigma = 2 * math.pi):
	x = np.random.normal(mu, sigma, size=(n,))
	y = np.sin(x)

	# return np.column_stack((x, y))
	return x, y
