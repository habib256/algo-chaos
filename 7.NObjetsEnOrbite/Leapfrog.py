import numpy as np
import matplotlib.pyplot as plt
    
# Solve x" = f(x) using leapfrog integrator
    
# For this demo, x'' + x = 0
# Exact solution is x(t) = sin(t)
def f(x):
    return -x
    
k = 5               # number of periods
N = 16              # number of time steps per period
h = 2*np.pi/N       # step size
    
x = np.empty(k*N+1) # positions
v = np.empty(k*N+1) # velocities
    
# Initial conditions
x[0] = 0
v[0] = 1
anew = f(x[0])
    
# leapfrog method
for i in range(1, k*N+1):
    aold = anew
    x[i] = x[i-1] + v[i-1]*h + 0.5*aold*h**2
    anew = f(x[i])
    v[i] = v[i-1] + 0.5*(aold + anew)*h

plt.show()
