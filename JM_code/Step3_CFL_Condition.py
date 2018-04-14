

import numpy                 #numpy is a library for array operations akin to MATLAB
from matplotlib import pyplot    #matplotlib is 2D plotting library


def linearconv(nx):
    dx = 2.0 / (nx - 1)
    nt = 20    #nt is the number of timesteps we want to calculate
    dt = .025  #dt is the amount of time each timestep covers (delta t)
    c = 1

    u = numpy.ones(nx)      #defining a numpy array which is nx elements long with every value equal to 1.
    u[int(.5/dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

    un = numpy.ones(nx) #initializing our placeholder array, un, to hold the values we calculate for the n+1 timestep

    for n in range(nt):  #iterate through time
        un = u.copy() ##copy the existing values of u into un
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
    pyplot.figure()    
    pyplot.plot(numpy.linspace(0, 2, nx), u);


# Now let's examine the results of our linear convection problem with an increasingly fine mesh.  

linearconv(41) #convection using 41 grid points

linearconv(61)

linearconv(71)

linearconv(85)


# In[8]:


def linearconv(nx):
    dx = 2.0 / (nx - 1)
    nt = 20    #nt is the number of timesteps we want to calculate
    c = 1       # this is the wave speed
    sigma = .5 # This is the condition on the CFL number
    
    dt = sigma * dx

    u = numpy.ones(nx) 
    u[int(.5/dx):int(1 / dx + 1)] = 2

    un = numpy.ones(nx)

    for n in range(nt):  #iterate through time
        un = u.copy() ##copy the existing values of u into un
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
            
    pyplot.figure()   
    pyplot.plot(numpy.linspace(0, 2, nx), u)


linearconv(41)

linearconv(61)

linearconv(81)

linearconv(101)

linearconv(121)


# Notice that as the number of points `nx` increases, the wave convects a shorter and shorter distance.
#  The number of time iterations we have advanced the solution at is held constant at `nt = 20`, 
# but depending on the value of `nx` and the corresponding values of `dx` and `dt`, a shorter time window is being examined overall.  
# It's possible to do rigurous analysis of the stability of numerical schemes, in some cases. 
#Watch Prof. Barba's presentation of this topic in **Video Lecture 9** on You Tube.




