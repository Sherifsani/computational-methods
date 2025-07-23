# import numpy as np

'''
splines are piecewise functions used to interpolate data points.
linear splines connect each pair of points with a straight line.
'''

def linear_spline(x, y, x_input):
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    
    if x[0] > x_input or x[-1] < x_input:
        raise ValueError("x_input must be within the range of x")
    
    length = len(x)
    
    for i in range(length - 1):
        if x[i] <= x_input <= x[i+1]:
            # compute slope
            slope = (y[i+1] - y[i])/(x[i+1] - x[i])
            y_output = y[i] + slope * (x_input - x[i])
            return y_output
    raise ValueError("could not find an appropriate interval")
    
