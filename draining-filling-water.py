from cmath import pi
import numpy as npx
import time
from ezGraph import *
from Cstats import *


# Parameters
dt = 1.
nsteps = 1000

r = 2.25 # radius (cm)
Q = 30 #Volume inflow rate (dv/dt): (cubic cm / s)
h = 0 #Initial heght(cm)
k = .15 # outflow rate constant(higher rate = faster outflow)


#Experimental Data

y_modeled = []


# Graph
graph = ezGraph(xmin=0, xmax=100, xLabel="Time (s)", yLabel="Height (cm)")
graph.add(0,h) #add


# Time loop
for t in range(1, nsteps):
    modelTime = t * dt

    #filling
    dh = (Q *dt)/(np.pi*r**2) # find change in height
    h = h + dh     # update heigth

    #draining
    dVdt = -k*h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    
    graph.add(modelTime, h)#(x,y)
    #graph.wait(0.01)#animates graph
print(modelTime, h)

#keeps graph open
graph.keepOpen() 