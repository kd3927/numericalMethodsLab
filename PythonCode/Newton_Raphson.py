def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    """
    Perform the Newton-Raphson Method to find a root of the function f.

    Parameters:
    f (function): The function for which to find the root.
    df (function): The derivative of the function f.
    x0 (float): The initial guess for the root.
    tol (float): The tolerance for the root approximation.
    max_iter (int): The maximum number of iterations.

    Returns:
    float: The approximate root of the function.
    """
    iter_count = 0
    error = float('inf')
    
    print(f"Iter |    x    |   f(x)  |   Error")
    print("------------------------------------")
    
    while error > tol and iter_count < max_iter:
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        
        x1 = x0 - fx / dfx
        error = abs(x1 - x0)
        
        print(f"{iter_count:4d} | {x0:.5f} | {fx:.5f} | {error:.5f}")
        
        x0 = x1
        iter_count += 1

    # Print the final iteration
    fx = f(x0)
    print(f"{iter_count:4d} | {x0:.5f} | {fx:.5f} | {error:.5f}")
    
    return x0

# Example usage
if __name__ == "__main__":
    # Define the function and its derivative
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1

    # Initial guess
    x0 = 1.5

    # Call the Newton-Raphson method
    root = newton_raphson(f, df, x0)
    print(f"\nRoot: {root}")
