import matplotlib.pyplot as plt
import numpy as np

def false_position(f, a, b):
    """
    Perform the False Position Method to find a root of the function f in the interval [a, b].
    
    Parameters:
    f (function): The function for which to find the root.
    a (float): The start of the interval.
    b (float): The end of the interval.
    tol (float): The tolerance for the root approximation.
    max_iter (int): The maximum number of iterations.
    
    Returns:
    float: The approximate root of the function.
    """
    tol=1e-5
    max_iter=100
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    iter_count = 0
    c_old = a  # Initialize to start of the interval
    error = float('inf')
    
    print(f"Iter |    a    |    b    |    c    |  f(c)    |  Error")
    print("-------------------------------------------------------")
    
    while error > tol and iter_count < max_iter:
        # Calculate the point c using the False Position formula
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        f_c = f(c)
        
        # Calculate the error
        error = abs(c - c_old)
        
        # Print the current iteration's results
        print(f"{iter_count:4d} | {a:.5f} | {b:.5f} | {c:.5f} | {f_c:.5f} | {error:.5f}")
        
        # Check if we've found the root
        if f_c == 0 or error < tol:
            return c
        
        # Update the interval
        if f(a) * f_c < 0:
            b = c
        else:
            a = c
        
        c_old = c
        iter_count += 1

    # Print the final iteration
    c = b - (f(b) * (b - a)) / (f(b) - f(a))
    f_c = f(c)
    print(f"{iter_count:4d} | {a:.5f} | {b:.5f} | {c:.5f} | {f_c:.5f} | {error:.5f}")
    
    return c

# Example usage
if __name__ == "__main__":
    # Define the function for which to find the root
    f = lambda x: x**3 - x - 2

    # Set the interval [a, b]
    a = 1
    b = 2

    # Call the False Position method
    root = false_position(f, a, b)
    print(f"\nRoot: {root}")

     # Plot the function and root
    x_vals = np.linspace(a, b, 100)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.scatter(root, f(root), color='red', marker='o')
    plt.axhline(y=0, color='gray', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method')
    plt.legend()
    plt.grid(True)
    plt.show()

