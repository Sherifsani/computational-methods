import math
from typing import Callable, Tuple, Optional


def newton_raphson(func: Callable[[float], float], 
                  derivative: Callable[[float], float], 
                  x0: float, 
                  tolerance: float = 1e-6, 
                  max_iterations: int = 100,
                  verbose: bool = True) -> Tuple[Optional[float], int, list]:
    """
    Newton-Raphson method for finding roots of a function.
    
    Parameters:
    -----------
    func : callable
        The function for which to find the root
    derivative : callable
        The derivative of the function
    x0 : float
        Initial guess
    tolerance : float, optional
        Convergence tolerance (default: 1e-6)
    max_iterations : int, optional
        Maximum number of iterations (default: 100)
    verbose : bool, optional
        Whether to print iteration details (default: True)
    
    Returns:
    --------
    tuple : (root, iterations, history)
        - root: The found root (None if not converged)
        - iterations: Number of iterations used
        - history: List of x values during iteration
    """
    x = x0
    history = [x]
    
    if verbose:
        print(f"Newton-Raphson Method")
        print(f"Initial guess: x0 = {x0}")
        print(f"Tolerance: {tolerance}")
        print("-" * 50)
    
    for i in range(max_iterations):
        fx = func(x)
        dfx = derivative(x)
        
        if verbose:
            print(f"Iteration {i+1:2d}: x = {x:10.6f}, f(x) = {fx:10.6f}, f'(x) = {dfx:10.6f}")
        
        # Check if we've found the root
        if abs(fx) < tolerance:
            if verbose:
                print(f"\nRoot found: x = {x:.6f}")
                print(f"Function value at root: f({x:.6f}) = {fx:.6e}")
                print(f"Converged in {i+1} iterations")
            return x, i+1, history
        
        # Check if derivative is too small (potential division by zero)
        if abs(dfx) < 1e-12:
            if verbose:
                print(f"\nDerivative too small: f'(x) = {dfx:.6e}")
                print("Method may not converge - derivative near zero")
            return None, i+1, history
        
        # Newton-Raphson update
        x_new = x - fx / dfx
        
        # Check for convergence based on change in x
        if abs(x_new - x) < tolerance:
            if verbose:
                print(f"\nRoot found: x = {x_new:.6f}")
                print(f"Function value at root: f({x_new:.6f}) = {func(x_new):.6e}")
                print(f"Converged in {i+1} iterations")
            return x_new, i+1, history
        
        x = x_new
        history.append(x)
    
    if verbose:
        print(f"\nMethod did not converge after {max_iterations} iterations")
        print(f"Last value: x = {x:.6f}, f(x) = {func(x):.6e}")
    
    return None, max_iterations, history


def quadratic_example():
    """Example with quadratic function: f(x) = x² - 4x + 3"""
    def f(x):
        return x**2 - 4*x + 3
    
    def df(x):
        return 2*x - 4
    
    print("Example 1: Quadratic function f(x) = x² - 4x + 3")
    print("Analytical roots: x = 1 and x = 3")
    print()
    
    # Find root starting from x0 = 0
    print("Starting from x0 = 0:")
    root1, _, _ = newton_raphson(f, df, x0=0, verbose=True)
    print()
    
    # Find root starting from x0 = 4
    print("Starting from x0 = 4:")
    root2, _, _ = newton_raphson(f, df, x0=4, verbose=True)
    print()


def transcendental_example():
    """Example with transcendental function: f(x) = e^x - 2x - 1"""
    def f(x):
        return math.exp(x) - 2*x - 1
    
    def df(x):
        return math.exp(x) - 2
    
    print("Example 2: Transcendental function f(x) = e^x - 2x - 1")
    print()
    
    # Find root starting from x0 = 1
    root, _, _ = newton_raphson(f, df, x0=1, verbose=True)
    print()


def polynomial_example():
    """Example with cubic polynomial: f(x) = x³ - 2x - 5"""
    def f(x):
        return x**3 - 2*x - 5
    
    def df(x):
        return 3*x**2 - 2
    
    print("Example 3: Cubic polynomial f(x) = x³ - 2x - 5")
    print()
    
    # Find root starting from x0 = 2
    root, _, _ = newton_raphson(f, df, x0=2, verbose=True)
    print()


def trigonometric_example():
    """Example with trigonometric function: f(x) = cos(x) - x"""
    def f(x):
        return math.cos(x) - x
    
    def df(x):
        return -math.sin(x) - 1
    
    print("Example 4: Trigonometric function f(x) = cos(x) - x")
    print()
    
    # Find root starting from x0 = 0.5
    root, _, _ = newton_raphson(f, df, x0=0.5, verbose=True)
    print()


def custom_function_example():
    """Example showing how to use the method with any custom function"""
    print("Example 5: Custom function f(x) = x³ - x - 1")
    print("Let's find the real root of this cubic equation")
    print()
    
    def f(x):
        return x**3 - x - 1
    
    def df(x):
        return 3*x**2 - 1
    
    # Try different starting points
    starting_points = [0, 1, 2, -1]
    
    for x0 in starting_points:
        print(f"Starting from x0 = {x0}:")
        root, iterations, history = newton_raphson(f, df, x0=x0, verbose=False)
        if root is not None:
            print(f"  Root found: x = {root:.6f} in {iterations} iterations")
            print(f"  Verification: f({root:.6f}) = {f(root):.6e}")
        else:
            print(f"  Did not converge from x0 = {x0}")
        print()


if __name__ == "__main__":
    print("Newton-Raphson Method Implementation")
    print("=" * 50)
    print()
    
    # Run examples
    quadratic_example()
    print("\n" + "="*50 + "\n")
    
    transcendental_example()
    print("\n" + "="*50 + "\n")
    
    polynomial_example()
    print("\n" + "="*50 + "\n")
    
    trigonometric_example()
    print("\n" + "="*50 + "\n")
    
    custom_function_example()
    
    print("=" * 50)
    print("Newton-Raphson Method Summary:")
    print("- Formula: x_{n+1} = x_n - f(x_n)/f'(x_n)")
    print("- Requires: function f(x) and its derivative f'(x)")
    print("- Converges quadratically when close to a simple root")
    print("- May fail if f'(x) = 0 or if starting point is poor")
    print("=" * 50)
