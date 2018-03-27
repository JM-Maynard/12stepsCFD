"""
Created on Wed Mar 14 20:54:57 2018

@author: Joshua

This is Step 2 in the 12 steps to CFD code. It demonstrates the non-linear convection equation
"""

import numpy                 #we're importing numpy and calling it np locally
from matplotlib import pyplot    #and our 2D plotting library, calling it plt
get_ipython().magic(u'matplotlib inline')


nx = 41
dx = 2.0 / (nx - 1)
nt = 20    #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)

u = numpy.ones(nx)      #as before, we initialize u with every value equal to 1.
u[int(.5 / dx) : int(1 / dx + 1)] = 2  #then set u = 2 between 0.5 and 1 as per our I.C.s

un = numpy.ones(nx) #initialize our placeholder array un, to hold the time-stepped solution


for n in range(nt):  #iterate through time
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx):  ##now we'll iterate through the u array 
           u[i] = un[i] - (un[i] * (dt / dx)) * (un[i] - un[i-1]) 
pyplot.plot(numpy.linspace(0, 2, nx), u) ##Plot the results
        


