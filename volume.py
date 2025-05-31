import numpy as np

# Define the function
def z(x, y):
    return x**2 + y**2

# Create grid
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
dx = dy = x[1] - x[0]

# Meshgrid
X, Y = np.meshgrid(x, y)
Z = z(X, Y)

# Approximate integral (volume)
volume = np.sum(Z) * dx * dy
print("Approximate Volume:", volume)
