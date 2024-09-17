def trapezoidal(f, a, b):
    """
    Perform the Trapezoidal Rule for a single interval [a, b].
    
    Parameters:
    f (function): The function to integrate.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    
    Returns:
    float: The approximate integral using the trapezoidal rule.
    """
    return (b - a) * (f(a) + f(b)) / 2

def composite_trapezoidal(f, a, b, n):
    """
    Perform the Composite Trapezoidal Rule for n subintervals.
    
    Parameters:
    f (function): The function to integrate.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    n (int): The number of subintervals.
    
    Returns:
    float: The approximate integral using the composite trapezoidal rule.
    """
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n):
        result += 2 * f(a + i * h)
    
    return (h / 2) * result

def simpsons_one_third(f, a, b, n):
    """
    Perform Simpson's 1/3 Rule for n subintervals (n must be even).
    
    Parameters:
    f (function): The function to integrate.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    n (int): The number of subintervals (must be even).
    
    Returns:
    float: The approximate integral using Simpson's 1/3 rule.
    """
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule.")
    
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        result += 2 * f(a + i * h)
    
    return (h / 3) * result

def simpsons_three_eighth(f, a, b, n):
    """
    Perform Simpson's 3/8 Rule for n subintervals (n must be a multiple of 3).
    
    Parameters:
    f (function): The function to integrate.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    n (int): The number of subintervals (must be a multiple of 3).
    
    Returns:
    float: The approximate integral using Simpson's 3/8 rule.
    """
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule.")
    
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 3 * f(a + i * h)
    
    return (3 * h / 8) * result

# Example usage
if __name__ == "__main__":
    f = lambda x: 1/x  # Function to integrate
    a = 1  # Lower limit
    b = 2  # Upper limit

    result = trapezoidal(f, a, b)
    print(f"Trapezoidal Rule Result: {result}")

    n = 4  # Number of subintervals
    result_ct = composite_trapezoidal(f, a, b, n)
    print(f"Composite Trapezoidal Rule Result: {result_ct}")

    result_s13 = simpsons_one_third(f, a, b, n)
    print(f"Simpson's 1/3 Rule Result: {result_s13}")

    n1 = 3  # Number of subintervals (must be a multiple of 3)
    result_s38 = simpsons_three_eighth(f, a, b, n1)
    print(f"Simpson's 3/8 Rule Result: {result_s38}")
