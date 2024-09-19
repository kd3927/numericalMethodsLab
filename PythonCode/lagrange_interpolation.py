def lagrange_interpolation(x_values, y_values, x):
    """
    Perform Lagrange interpolation.
    
    Parameters:
    x_values (list): List of known x-values.
    y_values (list): List of known y-values.
    x (float): The x-value to interpolate at.
    
    Returns:
    float: Interpolated y-value at x.
    """
    n = len(x_values)
    result = 0
    
    for i in range(n):
        # Compute the i-th Lagrange basis polynomial
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        
        # Add the contribution from the i-th term
        result += term
    
    return result

# Example usage
if __name__ == "__main__":
    # Example data points (x, y)
    x_values = [1, 2, 3, 4]
    y_values = [1, 4, 9, 16]
    
    # Interpolate the value at x = 2.5
    x_to_interpolate = 2.5
    interpolated_value = lagrange_interpolation(x_values, y_values, x_to_interpolate)
    
    print(f"Interpolated value at x = {x_to_interpolate}: {interpolated_value}")
