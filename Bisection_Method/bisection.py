import sympy as sp

x = sp.symbols('x')

def bisection(equation, a, b, tol=1e-6, max_iter=100, iter_count=0):
    f_a = equation.subs(x, a)
    f_b = equation.subs(x, b)

    if f_a * f_b > 0:
        print("f(a) * f(b) > 0. Bisection method cannot proceed. Try different a and b.")
        return None

    x_r = (a + b) / 2
    f_xr = equation.subs(x, x_r)

    print(f"Iteration {iter_count}: x = {x_r}, f(x) = {f_xr}")

    # Base conditions for stopping
    if abs(f_xr) < tol or abs(b - a) < tol or iter_count >= max_iter:
        print(f"Approximate root after {iter_count} iterations is: {x_r}")
        return x_r

    # Recursive step
    if f_a * f_xr < 0:
        return bisection(equation, a, x_r, tol, max_iter, iter_count + 1)
    else:
        return bisection(equation, x_r, b, tol, max_iter, iter_count + 1)

def main():
    equation = x**3 - 2*x - 5
    a = 2
    b = 3
    bisection(equation, a, b)

main()
