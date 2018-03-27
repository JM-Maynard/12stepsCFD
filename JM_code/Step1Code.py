# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:54:57 2018

@author: Joshua

This is Step 1 in the 12 steps to CFD code
"""


import numpy                       #here we load numpy
from matplotlib import pyplot      #here we load matplotlib
import time, sys                   #and load some utilities

nx = 41  # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2.0 / (nx-1)
nt = 50   #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)
c = 1      #assume wave speed =1

#Creation of the initial condition
u = numpy.ones(nx)      #numpy function ones()
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)

#Plotting initial conditions
pyplot.plot(numpy.linspace(0, 2, nx), u);

           
un = numpy.ones(nx) #initialize a temporary array

               
#Solution procedure               
for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx): ## you can try commenting this line and...
    #for i in range(nx): ## ... uncommenting this line and see what happens!
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
    
pyplot.plot(numpy.linspace(0, 2, nx), u);          
           
           