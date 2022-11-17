from cmath import pi
import numpy as npx
import time
from ezGraph import *
from Cstats import *

starttime = time.perf_counter()

# Parameters
dt = 1.
nsteps = 100

r = 2.25 # radius (cm)
Q = 30 #Volume inflow rate (dv/dt): (cubic cm / s)
h = 0 #Initial heght(cm)
k = .15 # outflow rate constant(higher rate = faster outflow)
dQ = -0.1
Qinitial = 30

#Experimental Data

y_modeled = []


# Graph
graph = ezGraph(xmin=0, xmax=100, xLabel="Time (s)", yLabel="Height (cm)")
graph.add(0,h) #add



# Time loop
for t in range(1, nsteps):
    modelTime = t * dt



    Q = 10*np.sin(50*modelTime) + 11

    #filling
    dh = (Q *dt)/(np.pi*r**2) # find change in height
    h = h + dh     # update heigth

    

    #draining
    dVdt = -k*h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

   

    

    
    graph.add(modelTime, h)#(x,y)
    #graph.wait(0.01)#animates graph

    #find max
    if (graph.y[-2] > graph.y[-1]) and (graph.y[-2]>graph.y[-3]):
        print(f"Max: {graph.y[-2]}")

#find min
    if modelTime > 1:
        if (graph.y[-2] < graph.y[-1]) and (graph.y[-2] < graph.y[-3]):
            print(f"Min: {graph.y[-2]}")




endtime = time.perf_counter()
print("runtime =", endtime-starttime)
#keeps graph open
graph.keepOpen() 