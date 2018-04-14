

import numpy
import sympy



from sympy import init_printing
init_printing(use_latex=True)

x, nu, t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
       sympy.exp(-(x - 4 * t - 2 * numpy.pi)**2 / (4 * nu * (t + 1))))
phi


# It's maybe a little small, but that looks right.  Now to evaluate our partial derivative $\frac{\partial \phi}{\partial x}$ is a trivial task.  

phiprime = phi.diff(x)
phiprime


# If you want to see the unrendered version, just use the Python print command.

# In[48]:

print(phiprime)



# 
# Now that we have the Pythonic version of our derivative, we can finish writing out the full initial condition equation and then translate it into a usable Python expression.  For this, we'll use the *lambdify* function, which takes a SymPy symbolic equation and turns it into a callable function.  

# In[49]:

from sympy.utilities.lambdify import lambdify

u = -2 * nu * (phiprime / phi) + 4
print(u)


# ### Lambdify
# 
# To lambdify this expression into a useable function, we tell lambdify which variables to request and the function we want to plug them in to.



ufunc = lambdify((t, x, nu), u)
print(ufunc(1, 4, 3))


# ### Back to Burgers' Equation
# 
# Now that we have the initial conditions set up, we can proceed and finish setting up the problem.  We can generate the plot of the initial condition using our lambdify-ed function.

# In[51]:

from matplotlib import pyplot


###variable declarations
nx = 101
nt = 100
dx = 2.0 * numpy.pi / (nx - 1)
nu = .07
dt = dx * nu

x = numpy.linspace(0, 2 * numpy.pi, nx)
un = numpy.empty(nx)
t = 0

u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])
u


# In[52]:

pyplot.figure(figsize=(11, 7), dpi=100)
pyplot.plot(x, u, marker='o', lw=2)
pyplot.xlim([0, 2 * numpy.pi])
pyplot.ylim([0, 10]);


# This is definitely not the hat function we've been dealing with until now. We call it a "saw-tooth function".  Let's proceed forward and see what happens.  

# ### Periodic Boundary Conditions
# 
# One of the big differences between Step 4 and the previous lessons is the use of *periodic* boundary conditions.  If you experiment with Steps 1 and 2 and make the simulation run longer (by increasing `nt`) you will notice that the wave will keep moving to the right until it no longer even shows up in the plot.  
# 
# With periodic boundary conditions, when a point gets to the right-hand side of the frame, it *wraps around* back to the front of the frame.  
# 
# Recall the discretization that we worked out at the beginning of this notebook:
# 
# $$u_i^{n+1} = u_i^n - u_i^n \frac{\Delta t}{\Delta x} (u_i^n - u_{i-1}^n) + \nu \frac{\Delta t}{\Delta x^2}(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$$
# 
# What does $u_{i+1}^n$ *mean* when $i$ is already at the end of the frame?
# 
# Think about this for a minute before proceeding.  
# 
# 



for n in range(nt): # looping over time
    un = u.copy()   # creating a copy to use for the iteration
    for i in range(1, nx-1): # looping over space
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 *                (un[i+1] - 2 * un[i] + un[i-1]) #looping over all of the internal nodes
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *                (un[1] - 2 * un[0] + un[-2]) #setting the value for the first node
    u[-1] = u[0] #setting the value for the last not
        
u_analytical = numpy.asarray([ufunc(nt * dt, xi, nu) for xi in x]) #calculating the analytical solution


# In[54]:

pyplot.figure(figsize=(11, 7), dpi=100)
pyplot.plot(x,u, marker='o', lw=2, label='Computational')
pyplot.plot(x, u_analytical, label='Analytical')
pyplot.xlim([0, 2 * numpy.pi])
pyplot.ylim([0, 10])
pyplot.legend();






