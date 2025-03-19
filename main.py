import numpy as np

# Given values
a = 0
b = 2
n = 10
delta_x = (b - a) / n

def f(x):
    # Change the formula here 
    # activity (a) formula -x**2
    return np.exp(-x**2) # Returns the f(x) value 
print("\n\n[Midpoint Rule]\n")
# Midpoint Rule x-values
x_midpoints = np.linspace(a + delta_x / 2, b - delta_x / 2, n)  # Midpoints of intervals
print(x_midpoints)
f_midpoint_values = f(x_midpoints)  # f(x) values at each midpoint
print(f_midpoint_values)

# Midpoint Rule sum
midpoint_integral = delta_x * np.sum(f_midpoint_values)
print("\n[Midpoint integral approximation]:", midpoint_integral)

print("\n\n[Trapezoid Rule]\n")
# Trapezoid Rule x-values
x_points = np.linspace(a, b, n+1) # Start, End, Number of instances
print(x_points)
f_values = f(x_points) # f(x) values at each point
print(f_values)

# Trapezoid Rule sum
trapezoid_integral = (delta_x / 2) * (f_values[0] + 2 * np.sum(f_values[1:-1]) + f_values[-1])
print("\n[Trapezoidal integral approximation]:", trapezoid_integral)