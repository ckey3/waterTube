from cmath import pi
import numpy as np
import time
from ezGraph import *
from Cstats import *

# model: something that imitates another closely that can predict the future
# Analytical model: equation or function that represents (best fits) the data (often use calculus to find the equations)
# physical models: small scale physical thing (you can touch it)
# numerical models: usally computer models becasue there's a lot of calculations (algebraic), 
# usally break the system into smaller parts that interact with each other, computer is used to keep track of all the interactions



# Finite Difference Model


# Parameters
dt = 1.
nsteps = 200

r = 2.25 # radius (cm)
Q = 0 #Volume inflow rate (dv/dt): (cubic cm / s)
h = 50 #Initial heght(cm)
k = .15 # outflow rate constant(higher rate = faster outflow)


#Experimental Data
x_measured = [0,28,60,101,157]
y_measured = [50,40,30,20,10]
y_modeled = [h]


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