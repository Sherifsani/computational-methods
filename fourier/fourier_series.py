import numpy as np
import matplotlib.pyplot as plt

# 🔢 QUESTION:
# Given a piecewise function defined on the interval (-π, π):
# f(t) = 0 for -π < t < 0
# f(t) = t for 0 <= t < π
#
# We want to approximate this function using its Fourier series expansion.
# Since the function is neither even nor odd, we compute:
# a0 (average term), an (cosine terms), and bn (sine terms).
# This code plots the original function and its Fourier approximation.

# 1. Define the original piecewise function
def f_original(t):
    # For t < 0 → 0, for t >= 0 → t
    return np.where(t < 0, 0, t)

# 2. Define the Fourier series approximation function
def f_fourier(t, N_terms=10):
    # a0 = π/4 is the average value of f(t) over [-π, π]
    a0 = np.pi / 4

    # Start the result array with just a0 (constant term)
    result = np.full_like(t, a0)

    # Add up the cosine and sine terms up to N_terms
    for n in range(1, N_terms + 1):
        # an = 0 for even n, an = -2 / (n^2 * π) for odd n
        if n % 2 == 1:
            an = -2 / (n**2 * np.pi)
        else:
            an = 0

        # bn = (-1)^(n+1) / n for all n
        bn = ((-1)**(n + 1)) / n

        # Add the term: an * cos(nt) + bn * sin(nt)
        result += an * np.cos(n * t) + bn * np.sin(n * t)

    return result

# 3. Create an array of t values from -π to π
t = np.linspace(-np.pi, np.pi, 1000)

# Evaluate the original function and the Fourier approximation
f_t = f_original(t)
approx = f_fourier(t, N_terms=10)

# 4. Plot the original function and its Fourier approximation
plt.figure(figsize=(10, 6))
plt.plot(t, f_t, label="Original function f(t)", color='black', linewidth=2)
plt.plot(t, approx, label="Fourier Approximation (10 terms)", linestyle='--', color='blue')

# Add labels, title, grid, and legend
plt.title("Fourier Series Approximation of a Piecewise Function")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)
plt.legend()
plt.show()
