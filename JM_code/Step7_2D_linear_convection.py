

# In[1]:

from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots

import numpy
from matplotlib import pyplot, cm


###variable declarations
nx = 161
ny = 161
nt = 100
c = 1
dx = 2.0 / (nx - 1)
dy = 2.0 / (ny - 1)
sigma = .2
dt = sigma * dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((ny, nx)) ##create a 1xn vector of 1's
un = numpy.ones((ny, nx)) ##

###Assign initial conditions

##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 

###Plot Initial Condition
##the figsize parameter can be used to produce different sized images
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')                      
X, Y = numpy.meshgrid(x, y)                            
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)



# ### 3D Plotting Notes

# To plot a projected 3D result, make sure that you have added the Axes3D library.  

#     from mpl_toolkits.mplot3d import Axes3D

# The actual plotting commands are a little more involved than with simple 2d plots.

# ```python
# fig = pyplot.figure(figsize=(11, 7), dpi=100)
# ax = fig.gca(projection='3d')
# surf2 = ax.plot_surface(X, Y, u[:])
# ```

# The first line here is initializing a figure window.  The **figsize** and **dpi** commands are optional and simply specify the size and resolution of the figure being produced.  You may omit them, but you will still require the 
#     
#     fig = pyplot.figure()
# 
# The next line assigns the plot window the axes label 'ax' and also specifies that it will be a 3d projection plot.  The final line uses the command
#     
#     plot_surface()
# 
# which is equivalent to the regular plot command, but it takes a grid of X and Y values for the data point positions.  
# 

# ##### Note
# 
# 
# The `X` and `Y` values that you pass to `plot_surface` are not the 1-D vectors `x` and `y`.  In order to use matplotlibs 3D plotting functions, you need to generate a grid of `x, y` values which correspond to each coordinate in the plotting frame.  This coordinate grid is generated using the numpy function `meshgrid`.
# 
#     X, Y = numpy.meshgrid(x, y)
# 
#  

# ### Iterating in two dimensions

# To evaluate the wave in two dimensions requires the use of several nested for-loops to cover all of the `i`'s and `j`'s.  Since Python is not a compiled language there can be noticeable slowdowns in the execution of code with multiple for-loops.  First try evaluating the 2D convection code and see what results it produces. 

# In[2]:

"""u = numpy.ones((ny, nx))
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1): ##loop across number of time steps
    un = u.copy()
    row, col = u.shape
    for j in range(1, row):
        for i in range(1, col):
            u[j, i] = (un[j, i] - (c * dt / dx * (un[j, i] - un[j, i - 1])) -
                                  (c * dt / dy * (un[j, i] - un[j - 1, i])))
            u[0, :] = 1
            u[-1, :] = 1
            u[:, 0] = 1
            u[:, -1] = 1

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)"""


# Array Operations
# ----------------
# 
# Here the same 2D convection code is implemented, but instead of using nested for-loops, the same calculations are evaluated using array operations.  

# In[3]:

u = numpy.ones((ny, nx))
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1): ##loop across number of time steps
    un = u.copy()
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                              (c * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)

    


