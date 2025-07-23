import numpy as np
import matplotlib.pyplot as plt

'''
This script demonstrates **Linear Spline Interpolation** using Python.

Splines are **piecewise functions** used to estimate values between known data points.
A **linear spline** connects each pair of points using straight lines, forming a continuous — but not smooth — curve.
'''

def linear_spline(x, y, x_input):
    """
    Estimate the y-value for a given x_input using linear spline interpolation.

    Parameters:
    x (list): A list of x-values (must be sorted in ascending order).
    y (list): A list of y-values corresponding to x.
    x_input (float): The x-value at which interpolation is desired.

    Returns:
    float: The estimated y-value at x_input.
    """
    
    # Make sure x and y are the same length
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    
    # Make sure x_input is within the interpolation range
    if x_input < x[0] or x_input > x[-1]:
        raise ValueError("x_input must be within the range of x")
    
    length = len(x)

    # Find the correct interval [x[i], x[i+1]] that contains x_input
    for i in range(length - 1):
        if x[i] <= x_input <= x[i+1]:
            # Compute the slope of the line segment
            slope = (y[i+1] - y[i]) / (x[i+1] - x[i])
            # Use the line equation to estimate y at x_input
            y_output = y[i] + slope * (x_input - x[i])
            return y_output
    
    # In case something went wrong (should not happen if x_input is valid)
    raise ValueError("Could not find an appropriate interval")


# Known data points
x_points = [1, 2, 3, 4]
y_points = [2, 3, 5, 4]

# Generate 100 equally spaced x-values between 1 and 4 for plotting the spline
x_vals = np.linspace(1, 4, 100)

# Calculate the corresponding y-values using the linear spline
y_vals = [linear_spline(x_points, y_points, x) for x in x_vals]

# Plot original data points as dots
plt.plot(x_points, y_points, 'o', label="Data Points")

# Plot the interpolated linear spline as a line
plt.plot(x_vals, y_vals, label="Linear Spline")

# Add legend, grid, title, and axis labels
plt.legend()
plt.grid(True)
plt.title("Linear Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")

# Show the plot
plt.show()
