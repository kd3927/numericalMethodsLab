import matplotlib.pyplot as plt

def mean(values):
    return sum(values) / len(values)

def linear_regression(x_values, y_values):
    """
    Perform linear regression to find the slope (m) and intercept (b).
    
    Parameters:
    x_values (list): List of independent variable values (x).
    y_values (list): List of dependent variable values (y).
    
    Returns:
    tuple: The slope (m) and intercept (b).
    """
    n = len(x_values)
    
    # Calculating sums required for the formula
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_x_squared = sum([x**2 for x in x_values])
    sum_xy = sum([x_values[i] * y_values[i] for i in range(n)])
    
    # Slope (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    
    # Intercept (b)
    b = (sum_y - m * sum_x) / n
    
    return m, b

def predict(x, m, b):
    """
    Predict y-value using the regression line equation.
    
    Parameters:
    x (float): Independent variable value.
    m (float): Slope of the line.
    b (float): Intercept of the line.
    
    Returns:
    float: Predicted y-value.
    """
    return m * x + b

# Example usage
if __name__ == "__main__":
    # Example data points (x, y)
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 5, 4, 5]
    
    # Perform linear regression to find the slope and intercept
    m, b = linear_regression(x_values, y_values)
    print(f"Slope (m): {m}")
    print(f"Intercept (b): {b}")
    
    # Predict y-value for a given x-value
    x_to_predict = float(input("Enter value of to predict y:"))
    predicted_y = predict(x_to_predict, m, b)
    print(f"Predicted y-value at x = {x_to_predict}: {predicted_y}")

    # Generate predicted y-values
    y_predicted = [predict(x, m, b) for x in x_values]
    
    # Plot the original data points
    plt.scatter(x_values, y_values, color='blue', label='Data Points')
    
    # Plot the regression line
    plt.plot(x_values, y_predicted, color='red', label='Regression Line')

    # Plot the predicted point
    plt.scatter(x_to_predict,predicted_y, color='k', marker='s', label='Predicted Point')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Regression')
    plt.legend()
    plt.grid(True)
    plt.show()
