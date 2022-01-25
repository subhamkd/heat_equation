# heat_equation
Python script for solving the transient heat equation in 2D using finite difference method.  
The script uses explicit forward euler time stepping with central differencing for space.  
The results are saved after a desired number of timesteps as .csv files.  
The saved results are used to make an animation of the transient behaviour.

## Heated Square example
simulating the heat distribution in a 1x1 square domain initially at 300K, with the top and right boundry at maintained at 100K.  

## Random heated square example
Simulating a square with different temperatures at different points (between 0 and 300), with insulated boundaries and letting the temperature distribution go towards equilibrium.