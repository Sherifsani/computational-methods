import matplotlib.pyplot as plt
import numpy as np

# example equation
# y = (3 * x**2)/(x**2 - 4)

# Limits as x approaches infinity
for x in [10, 100, 1000, 10000, 100000, 1000000]:
    limit = (3 * x**2)/(x**2 - 4)
    print(f"Limit as x approaches {x}: {limit}")

# Graphing the function
x = 0
y = (3 * x**2)/(x**2 - 4)

zoom = 10
x_min = x - zoom
x_max = x + zoom
y_min = y - zoom
y_max = y + zoom

x_vals = np.linspace(x_min, x_max, 100)
y_vals = (3 * x_vals**2)/(x_vals**2 - 4)

plt.axis([x_min, x_max, y_min, y_max])
plt.plot(x_vals, y_vals)
plt.plot([x], [y], 'ro')  # mark the point (x, y)
plt.axhline(y=0, color='k')
plt.axhline(x=0, color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = (3 * x^2)/(x^2 - 4)')
plt.show()