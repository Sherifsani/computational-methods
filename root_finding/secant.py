import sympy as sp

x = sp.symbols('x')

def secant(equation, a, b, epsilon = 1e-6, max_iteration=100, iteration_count=0):
    f_a = equation.subs(x,a)
    f_b = equation.subs(x,b)

    x_new = float(b - (f_b * ((b - a) / (f_b - f_a))))
    f_x_new = equation.subs(x, x_new)

    print(f"iteration {iteration_count}: x = {x_new:.5} | f(x) = {f_x_new:.5}")

    if abs(f_x_new) < epsilon or abs(b - a) < epsilon or iteration_count >= max_iteration:
        print(f"Approximate root after {iteration_count} iterations is: {x_new}")
        return x_new
    else:
        return secant(equation, b, x_new, epsilon, max_iteration, iteration_count + 1)

def main():
    equation = x**3 - 2*x - 5
    secant(equation, 2, 3)


main()
