import sympy
from sympy import symbols
from sympy.solvers import solve

# Where is the function undefined?
# example function 
# y = (3 * x**2)/(x**2 - 4)

x = symbols('x')

# put the equation here
eqn = x**2 - 4

print("undefined at x = ", solve(eqn))

# Limits approaching right or left
x = 2 
h = 0.0001

y_right = 3 * ((x + h)**2) / ((x + h)**2 - 4)
y_left = 3 * ((x - h)** 2) / ((x - h)**2 - 4)

print("y_left: ", y_left)
print("y_right: ", y_right)

if round(y_right) != round(y_left):
    print("Limit does not exist at x = ", x)