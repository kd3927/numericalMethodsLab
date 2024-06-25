def bisection(f, a, b, tol=1e-5, max_iter=100):
    """
    Perform the Bisection Method to find a root of the function f in the interval [a, b].

    Parameters:
    f (function): The function for which to find the root.
    a (float): The start of the interval.
    b (float): The end of the interval.
    tol (float): The tolerance for the root approximation.
    max_iter (int): The maximum number of iterations.

    Returns:
    float: The approximate root of the function.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    iter_count = 0
    error = abs(b - a) / 2.0
    
    print(f"Iter |    a    |    b    |    c    |  f(c)  |  Error")
    print("-------------------------------------------------------")
    
    while error > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        f_c = f(c)
        print(f"{iter_count:4d} | {a:.5f} | {b:.5f} | {c:.5f} | {f_c:.5f} | {error:.5f}")
        
        if f_c == 0:  # We've found the root exactly
            return c
        elif f(a) * f_c < 0:
            b = c
        else:
            a = c
        
        error = abs(b - a) / 2.0
        iter_count += 1

    # Print the final iteration
    c = (a + b) / 2.0
    f_c = f(c)
    print(f"{iter_count:4d} | {a:.5f} | {b:.5f} | {c:.5f} | {f_c:.5f} | {error:.5f}")
    
    return c  # Return the midpoint as the best approximation

# Example usage
if __name__ == "__main__":
    # Define the function for which to find the root
    f = lambda x: x**3 - x - 2

    # Set the interval [a, b]
    a = 1
    b = 2

    # Call the bisection method
    root = bisection(f, a, b)
    print(f"\nRoot: {root}")
