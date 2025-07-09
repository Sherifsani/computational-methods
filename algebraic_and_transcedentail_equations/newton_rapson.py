import sympy as sp

def newton_rapson(a, b, c, x = 1):
    fx = (a * x * x) - (b * x) + c
    print(f"f(x) is {fx}")
    
    if fx == 0:
        return f"x = {x} is a root of the equation"
    else:
        print(f"{x} is not a root")
        f_dx = (2 * a * x) - b

        print(f"dervivative value is {f_dx}")
        x2 = x - (fx/f_dx)

        print(f"the next value of x is {x2}")
        return newton_rapson(a, b, c, x2)

print(newton_rapson(1, -1, 6, 1))