import os
# import numpy as np

def __init__():
    package_name = 'numpy'  # Replace with the package name

    try:
        import numpy as np
        print(f"{package_name} is installed!\n")
    except ImportError:
        print(f"{package_name} is not installed.\nInstalling it for you. ( required )")
        os.system(f"pip install {package_name}")

__init__()
import numpy as np

def main():
    # Given values
    a = 0
    b = 2
    n = 10
    delta_x = (b - a) / n
    MidPoint(a, b, n, delta_x)
    Trapezoid(a, b, n, delta_x)
    Simpson(a, b, 20, delta_x)



def f(x):
    # Change the formula here 
    # activity (a) formula -x**2
    return np.exp(-x**2) # Returns the f(x) value

def MidPoint(a, b, n, delta_x): # Midpoint Rule
    print("\n\n[Midpoint Rule]\n")
    # Midpoint Rule x-values
    x_midpoints = np.linspace(a + delta_x / 2, b - delta_x / 2, n)  # Midpoints of intervals
    print(x_midpoints)
    f_midpoint_values = f(x_midpoints)  # f(x) values at each midpoint
    print(f_midpoint_values)

    # Midpoint Rule sum
    midpoint_integral = delta_x * np.sum(f_midpoint_values)
    print("\n[Midpoint integral approximation]:", midpoint_integral)

def Trapezoid(a, b, n, delta_x): # Trapezoid Method
    print("\n\n[Trapezoid Rule]\n")
    # Trapezoid Rule x-values
    x_points = np.linspace(a, b, n+1) # Start, End, Number of instances
    print(x_points)
    f_values = f(x_points) # f(x) values at each point
    print(f_values)

    # Trapezoid Rule sum
    trapezoid_integral = (delta_x / 2) * (f_values[0] + 2 * np.sum(f_values[1:-1]) + f_values[-1])
    print("\n[Trapezoidal integral approximation]:", trapezoid_integral )

def Simpson(a, b, n, delta_x):
    print("\n\n[Simpson Rule]\n")
    #Simpson Rule x-values
    x_points = np.linspace(a, b, n+1) # Start, End, Number of instances
    print(x_points)
    f_values = f(x_points)
    print(f_values)

    # Setting odd or even values
    odd_sum = np.sum(f_values[1:-1:2])  # Suma de los valores en las posiciones impares (x1, x3, x5,...)
    even_sum = np.sum(f_values[2:-1:2])

    simpson_integral = delta_x / 3 * (f_values[0] + f_values[-1] + 4 * odd_sum + 2 * even_sum)
    print("[Simpson's integral approximation]:", simpson_integral)

# Runners
__init__()
main()
