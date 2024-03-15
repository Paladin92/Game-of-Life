Conway's Game of Life Simulation
Overview
This project implements a Python simulation of Conway's Game of Life using NumPy for grid manipulation, Matplotlib for visualization, and Tkinter for obtaining screen dimensions. Conway's Game of Life is a cellular automaton where cells on a grid evolve at each step according to simple rules based on their neighbors' states.

Requirements
Python 3
NumPy
Matplotlib
Tkinter (usually included with Python)
Installation
Ensure you have Python 3 installed on your system. You can then install the required packages using pip:


pip install numpy matplotlib
Tkinter is typically included with Python, but if you're missing it, you might need to install it separately depending on your operating system.

Running the Simulation
To run the simulation, simply execute the script:


python game_of_life.py
The simulation will start in a fullscreen window on your main monitor. The initial state of the grid is random, with each cell having a 10% chance of being alive.

How It Works
The simulation grid is a square of size N x N, where N is set to 100 by default. Each cell in the grid can either be alive (white) or dead (black), represented by 255 and 0 in the grid array, respectively.

At each step of the simulation, the script updates the state of each cell based on the following rules:

A live cell with fewer than two live neighbors dies (underpopulation).
A live cell with two or three live neighbors lives on to the next generation.
A live cell with more than three live neighbors dies (overpopulation).
A dead cell with exactly three live neighbors becomes alive (reproduction).
These rules are applied simultaneously to every cell in the grid, creating various patterns that can move, oscillate, or remain static.

Customization
You can modify the size of the grid or the probability of a cell being alive at the start by adjusting the N and p values, respectively, in the np.random.choice function call.

Enjoy exploring Conway's Game of Life!
