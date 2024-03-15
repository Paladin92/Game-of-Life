import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    # Copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Compute 8-neighbor sum using toroidal boundary conditions
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
           
            # Apply Conway's rules
            if grid[i, j] == 255:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 255
   
    # Update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Main code
N = 100
grid = np.random.choice([0, 255], N*N, p=[0.9, 0.1]).reshape(N, N)

# Get the screen resolution of the main monitor
import tkinter as tk
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Create a figure with the size of the main monitor
fig = plt.figure(figsize=(screen_width/100, screen_height/100), dpi=100)

# Remove the toolbar from the figure
fig.canvas.toolbar_visible = False

# Make the plot occupy the entire figure
ax = fig.add_axes([0, 0, 1, 1])

img = ax.imshow(grid, interpolation='nearest')

# Remove the axis ticks and labels
ax.axis('off')

ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                              frames=10,
                              interval=50,
                              save_count=50)

# Make the plot window fullscreen
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.show()
