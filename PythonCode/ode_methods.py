import matplotlib.pyplot as plt
#import numpy as np

def euler_method(f, x0, y0, h, n):
    """
    Euler's Method for solving y' = f(x, y).
    
    Parameters:
    f (function): The derivative function y' = f(x, y).
    x0 (float): Initial value of x.
    y0 (float): Initial value of y.
    h (float): Step size.
    n (int): Number of steps.
    
    Returns:
    list: List of x and y values.
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)
    
    return x_values, y_values

def heuns_method(f, x0, y0, h, n):
    """
    Heun's Method (Improved Euler) for solving y' = f(x, y).
    
    Parameters:
    f (function): The derivative function y' = f(x, y).
    x0 (float): Initial value of x.
    y0 (float): Initial value of y.
    h (float): Step size.
    n (int): Number of steps.
    
    Returns:
    list: List of x and y values.
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        # Predictor step (Euler's estimate)
        y_predict = y0 + h * f(x0, y0)
        
        # Corrector step (average the slopes)
        y0 = y0 + (h / 2) * (f(x0, y0) + f(x0 + h, y_predict))
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)
    
    return x_values, y_values

def rk4_method(f, x0, y0, h, n):
    """
    Runge-Kutta 4th Order (RK4) Method for solving y' = f(x, y).
    
    Parameters:
    f (function): The derivative function y' = f(x, y).
    x0 (float): Initial value of x.
    y0 (float): Initial value of y.
    h (float): Step size.
    n (int): Number of steps.
    
    Returns:
    list: List of x and y values.
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        
        y0 = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)
    
    return x_values, y_values

# Example usage
if __name__ == "__main__":
    f = lambda x,y: x+y**2  # Example ODE y' = x + y
    x0 = 0  # Initial x
    y0 = 1  # Initial y
    h = 0.1  # Step size
    n = 5  # Number of steps

    x_vals_eu, y_vals_eu = euler_method(f, x0, y0, h, n)
    print("<<<< Euler's Method Solution >>>>>")
    for x, y in zip(x_vals_eu, y_vals_eu):
        print(f"x: {x:.2f}, y: {y:.5f}")

    x_vals_h, y_vals_h = heuns_method(f, x0, y0, h, n)
    print("<<<< Heun's Method Solution >>>>>")
    for x, y in zip(x_vals_h, y_vals_h):
        print(f"x: {x:.2f}, y: {y:.5f}")

    x_vals_rk, y_vals_rk = rk4_method(f, x0, y0, h, n)
    print("<<<< RK4 Method Solution >>>>>")
    for x, y in zip(x_vals_rk, y_vals_rk):
        print(f"x: {x:.2f}, y: {y:.5f}")

    # Plot all methods
    plt.plot(x_vals_eu, y_vals_eu, label="Euler's Method", marker='o')
    plt.plot(x_vals_h, y_vals_h, label="Heun's Method", marker='s')
    plt.plot(x_vals_rk, y_vals_rk, label="RK4 Method", marker='^')
    
    plt.title("Comparison of Numerical Methods for ODE")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
