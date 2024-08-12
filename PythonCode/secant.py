def secant_method(f, x0, x1):
    """
    Perform the Secant Method to find a root of the function f.
    
    Parameters:
    f (function): The function for which to find the root.
    x0 (float): The first initial guess for the root.
    x1 (float): The second initial guess for the root.
    tol (float): The tolerance for the root approximation.
    max_iter (int): The maximum number of iterations.
    
    Returns:
    float: The approximate root of the function.
    """
    tol=1e-5
    max_iter=100
    iter_count = 0
    error = float('inf')
    
    print(f"Iter |    x0   |    x1   |    x2   |    f(x2)   |  Error")
    print("----------------------------------------------------------")
    
    while error > tol and iter_count < max_iter:
        # Calculate the next approximation of the root using the Secant formula
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            raise ValueError("Division by zero: f(x1) and f(x0) are equal.")
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        f_x2 = f(x2)
        
        # Calculate the error
        error = abs(x2 - x1)
        
        # Print the current iteration's results
        print(f"{iter_count:4d} | {x0:.5f} | {x1:.5f} | {x2:.5f} | {f_x2:.5f} | {error:.5f}")
        
        # Update points for the next iteration
        x0 = x1 
        x1 = x2
        iter_count += 1
    
    # Print the final iteration
    print(f"{iter_count:4d} | {x0:.5f} | {x1:.5f} | {x2:.5f} | {f_x2:.5f} | {error:.5f}")
    
    return x2

# Example usage
if __name__ == "__main__":
    # Define the function for which to find the root
    f = lambda x: x**3 - x - 2
    
    # Set the initial guesses
    x0 = 1.0
    x1 = 2.0
    
    # Call the Secant method
    root = secant_method(f, x0, x1)
    print(f"\nRoot: {root}")
