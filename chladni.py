# A Simple Python Simulation of various Chladni Figures.
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Define the number of points in the grid (Resolution)
N = 500

# Create the grid
plate_size = 1.5
x = np.linspace(-plate_size, plate_size, N)
y = np.linspace(-plate_size, plate_size, N)

# Find the amplitude of the wave at a given point
def amplitude(x, y, n, m):
    # \sin\left(n\pi x\right)\sin\left(m\pi y\right)-\sin\left(m\pi x\right)\sin\left(n\pi y\right)
    return np.sin(n*np.pi*x)*np.sin(m*np.pi*y) - np.sin(m*np.pi*x)*np.sin(n*np.pi*y)

# Find the amplitude at every x,y point using the amplitude function
def amplitude_grid(x, y, n, m):
    # Create a grid of zeros
    z = np.zeros((N,N))
    # Loop over the grid
    for i in range(N):
        for j in range(N):
            z[i,j] = amplitude(x[i], y[j], n, m)
    return z

# Plot the amplitude grid
def plot_amplitude_grid(x, y, n, m):
    # Create the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Define the colormap to use ()
    # cmap = 'RdYlBu_r'
    cmap = 'twilight'
    
    # Plot the amplitude grid 
    contour = ax.contourf(x, y, amplitude_grid(x, y, n, m), 100, cmap=cmap)

    # Show the colorbar for the colormap
    plt.colorbar(contour)

    # Set the title
    ax.set_title('n = ' + str(n) + ', m = ' + str(m))

    # Show the plot
    # plt.show()
    plt.savefig(f'plots\\n={n}_m={m}.png')
    plt.close()


# Plot the amplitude grid for a given n and m
for i in range(1, 11):
    for j in tqdm(range(1, 11)):
        plot_amplitude_grid(x, y, i, j)
