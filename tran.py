import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the transcendental equation components
def lhs(z):
    return -1 / np.tan(z)

def rhs(z, a):
    return np.sqrt((a / z)**2 - 1)

# Plot the functions
def plot_functions(a, z_min, z_max, num_points=1000):
    z_values = np.linspace(z_min, z_max, num_points)
    
    # Calculate LHS and RHS
    lhs_values = lhs(z_values)
    rhs_values = rhs(z_values, a)
    
    # Plot the functions
    plt.figure(figsize=(10, 6))
    plt.plot(z_values, lhs_values, label='-cot(z)')
    plt.plot(z_values, rhs_values, label=f'1 / sqrt((a/z)^2 - 1) with a={a}')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.ylim(-10, 10)  # Limit y-axis to avoid extreme values in plot
    plt.xlim(z_min, z_max)
    plt.legend()
    plt.xlabel('z')
    plt.ylabel('Function Value')
    plt.title('Plot of LHS and RHS of the Transcendental Equation')
    plt.grid(True)
    plt.show()


# Find intersection points
def find_intersections(a, z_initial_guesses):
    intersections = []
    for z_guess in z_initial_guesses:
        z_intersect = fsolve(lambda z: lhs(z) - rhs(z, a), z_guess)
        if z_intersect not in intersections:  # To avoid duplicates
            intersections.append(z_intersect[0])
    return intersections


# Parameters
a = 5  # Example value for a
z_min = 0  # Avoid division by zero
z_max = 10

# Initial guesses for finding intersections
z_initial_guesses = np.linspace(z_min, z_max, 50)

# Plot the functions
plot_functions(a, z_min, z_max)

# Find and print intersection points
intersections = find_intersections(a, z_initial_guesses)
print(f"Intersection points for a={a}: {intersections}")