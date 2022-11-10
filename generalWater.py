from cmath import pi
import numpy as np
import time
from ezGraph import *

# Finite Difference Modelmodel
# 

# Parameters
dt = 1.
nsteps = 50

r = 2.25 # radius (cm)
Q = 20 #Volume inflow rate (dv/dt): (cubic cm / s)
h = 0 #Initial heght(cm)
k = 1.0 # outflow rate constant(higher rate = faster outflow)


# Graph
graph = ezGraph(xmax=30, ymin=0, ymax=10,xLabel="Time (s)", yLabel="Height (cm)")#xmax = 30 (changes the x length)

# Time loop
for t in range(nsteps):
    modelTime = t * dt

    #filling
    dh = (Q *dt)/(pi*r**2) # find change in height
    h = h + dh     # update heigth

    #draining
    dVdt = -k*h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    print(modelTime, h)#(time, hieght)
    graph.add(modelTime, h)#(x,y)
    graph.wait(0.1)#animates graph

graph.keepOpen() #keeps graph open

