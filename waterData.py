import numpy as np
import time
from ezGraph import *

# model


# Parameters
dt = 1.
nsteps = 50

# linear model
m = -10.3
b = 45.8

# Graph
graph = ezGraph(xmax=30, ymin=0, ymax=50,xLabel="Time (s)", yLabel="Height (cm)")#xmax = 30 (changes the x length)

# Time loop
for t in range(nsteps):
    modelTime = t * dt
    h = m*modelTime+b
    print(modelTime, h)#(time, hieght)
    graph.add(modelTime, h)#(x,y)
    graph.wait(0.1)#animates graph

graph.keepOpen() #keeps graph open

