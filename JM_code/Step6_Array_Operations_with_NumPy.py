
# ----------------
# 
# For more computationally intensive programs, the use of built-in Numpy functions can provide an  increase in execution speed many-times over.  As a simple example, consider the following equation:
# 
# $$u^{n+1}_i = u^n_i-u^n_{i-1}$$
# 
# Now, given a vector $u^n = [0, 1, 2, 3, 4, 5]\ \ $   we can calculate the values of $u^{n+1}$ by iterating over the values of $u^n$ with a for loop.  

# In[1]:

import numpy


# In[2]:

u = numpy.array((0, 1, 2, 3, 4, 5))

for i in range(1, len(u)):
    print(u[i] - u[i-1])


# This is the expected result and the execution time was nearly instantaneous.  If we perform the same operation as an array operation, then rather than calculate $u^n_i-u^n_{i-1}\ $ 5 separate times, we can slice the $u$ array and calculate each operation with one command:

# In[3]:

u[1:] - u[0:-1]


# What this command says is subtract the 0th, 1st, 2nd, 3rd, 4th and 5th elements of $u$ from the 1st, 2nd, 3rd, 4th, 5th and 6th elements of $u$.  
# 
# ### Speed Increases
# 
# For a 6 element array, the benefits of array operations are pretty slim.  There will be no appreciable difference in execution time because there are so few operations taking place.  But if we revisit 2D linear convection, we can see some substantial speed increases.  
# 

# In[4]:

nx = 81
ny = 81
nt = 100
c = 1
dx = 2.0 / (nx - 1)
dy = 2.0 / (ny - 1)
sigma = .2
dt = sigma * dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((ny, nx)) ##create a 1xn vector of 1's
un = numpy.ones((ny, nx)) 

###Assign initial conditions

u[int(.5 / dy): int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2


# With our initial conditions all set up, let's first try running our original nested loop code, making use of the iPython "magic" function `%%timeit`, which will help us evaluate the performance of our code. 
# 
# **Note**: The `%%timeit` magic function will run the code several times and then give an average execution time as a result.  If you have any figures being plotted within a cell where you run `%%timeit`, it will plot those figures repeatedly which can be a bit messy. 

# In[5]:

get_ipython().run_cell_magic(u'timeit', u'', u'u = numpy.ones((ny, nx))\nu[int(.5 / dy): int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2\n\nfor n in range(nt + 1): ##loop across number of time steps\n    un = u.copy()\n    row, col = u.shape\n    for j in range(1, row):\n        for i in range(1, col):\n            u[j, i] = (un[j, i] - (c * dt / dx * \n                                  (un[j, i] - un[j, i - 1])) - \n                                  (c * dt / dy * \n                                   (un[j, i] - un[j - 1, i])))\n            u[0, :] = 1\n            u[-1, :] = 1\n            u[:, 0] = 1\n            u[:, -1] = 1')


# With the "raw" Python code above, the best execution time achieved was 1.94 seconds.  Keep in mind that with these three nested loops, that the statements inside the **j** loop are being evaluated more than 650,000 times.   Let's compare that with the performance of the same code implemented with array operations:

# In[6]:

get_ipython().run_cell_magic(u'timeit', u'', u'u = numpy.ones((ny, nx))\nu[int(.5 / dy): int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2\n\nfor n in range(nt + 1): ##loop across number of time steps\n    un = u.copy()\n    u[1:, 1:] = un[1:, 1:] - ((c * dt / dx * (un[1:, 1:] - un[1:, 0:-1])) -\n                              (c * dt / dy * (un[1:, 1:] - un[0:-1, 1:])))\n    u[0, :] = 1\n    u[-1, :] = 1\n    u[:, 0] = 1\n    u[:, -1] = 1')


# As you can see, the speed increase is substantial.  The same calculation goes from 1.94 seconds to 5.09 milliseconds.  2 seconds isn't a huge amount of time to wait, but these speed gains will increase exponentially with the size and complexity of the problem being evaluated.  

# In[7]:

from IPython.core.display import HTML
def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()


# In[ ]:



