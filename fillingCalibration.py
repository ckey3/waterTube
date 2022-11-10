from cmath import pi
import numpy as np
import time
from ezGraph import *
from Cstats import *

# Finite Difference Model


# Parameters
dt = 1.
nsteps = 30

r = 2.25 # radius (cm)
Q = 30 #Volume inflow rate (dv/dt): (cubic cm / s)
h = -2 #Initial heght(cm)
k = 0.0 # outflow rate constant(higher rate = faster outflow)

#Experimental Data
x_measured = [1,7,12,17,22,26]
y_measured = [0,10,20,30,40,50]
y_modeled = []


# Graph
graph = ezGraphMM(xmin=0, xmax=100, xLabel="Time (s)", yLabel="Height (cm)", x_measured = x_measured, y_measured = y_measured)

graph.addModeled(0,h) #add


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

    if (modelTime in x_measured):
       # print(modelTime, h)
        y_modeled.append(h)#put h into an array

   # print(x_measured, y_measured)#(time, hieght)
    graph.addModeled(modelTime, h)#(x,y)
    #graph.wait(0.01)#animates graph

print("y_measured:,", y_measured)
print("y_modeled:", y_modeled)

#print average values 
avg = avg1(y_measured)
avg2 = avg1(x_measured)
avg3 = avg1(y_modeled)
#print("avg y_measured:", avg)
#print("avg x_measured", avg2)
#print("avg y_modeled", avg3)

#print residual
r = residual(y_measured,y_modeled)
print("sum rediduals:", r)

#mean difference
m = meanDiff(y_measured)
print("sum of mean difference:", m)

# r^2
r2 = 1 - (r/m) #r2 = 1 - (residual(y_measured,y_modeled)/meanDiff(y_measured))
print("r^2:",r2)

#keeps graph open
graph.keepOpen() 