import numpy as np
import matplotlib.pyplot as plt

# Sample data points
x = [1, 2, 3, 4]
y = [2, 3, 5, 4]

# Number of intervals (n-1 splines for n points)
n = len(x) - 1

# Each spline has 3 coefficients: a, b, c for ai + bi*(x - xi) + ci*(x - xi)^2
# So we have 3*(n) unknowns
A = []
b_vec = []

# 1. Interpolation conditions: S(x_i) = y_i and S(x_{i+1}) = y_{i+1}
for i in range(n):
    xi, xi1 = x[i], x[i+1]
    yi, yi1 = y[i], y[i+1]

    # S(xi) = yi
    row = [0] * 3 * n
    row[3*i] = 1  # ai
    A.append(row)
    b_vec.append(yi)

    # S(xi1) = yi1
    row = [0] * 3 * n
    row[3*i] = 1                      # ai
    row[3*i+1] = (xi1 - xi)           # bi * (x - xi)
    row[3*i+2] = (xi1 - xi)**2        # ci * (x - xi)^2
    A.append(row)
    b_vec.append(yi1)

# 2. Smoothness condition: S'_i(x_{i+1}) = S'_{i+1}(x_{i+1})
for i in range(n - 1):
    xi, xi1 = x[i], x[i+1]
    row = [0] * 3 * n
    row[3*i + 1] = 1                        # bi
    row[3*i + 2] = 2 * (xi1 - xi)           # 2 * ci * (x - xi)
    row[3*(i+1) + 1] = -1                   # -b(i+1)
    A.append(row)
    b_vec.append(0)

# 3. Natural spline condition: c0 = 0
row = [0] * 3 * n
row[2] = 1  # c0
A.append(row)
b_vec.append(0)

# Solve the system
A = np.array(A, dtype=float)
b_vec = np.array(b_vec, dtype=float)
coeffs = np.linalg.solve(A, b_vec)

# Plotting the spline
x_vals = np.linspace(x[0], x[-1], 200)
y_vals = []

for val in x_vals:
    for i in range(n):
        if x[i] <= val <= x[i+1]:
            dx = val - x[i]
            a = coeffs[3*i]
            b = coeffs[3*i + 1]
            c = coeffs[3*i + 2]
            y_val = a + b*dx + c*dx**2
            y_vals.append(y_val)
            break

plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_vals, y_vals, label='Quadratic Spline')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Spline Interpolation")
plt.grid(True)
plt.legend()
plt.show()
