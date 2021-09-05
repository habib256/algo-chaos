import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

nmax = 30
r = 2.0
dr = 0.005
u0 = 0.7

xmin = 0
xmax = nmax

x = np.linspace(xmin, xmax, nmax)

fig = plt.figure() # initialise la figure
line, = plt.plot([],[]) 
plt.xlim(xmin, xmax)
plt.ylim(0,1)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def u(n,r):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

def animate(i): 
    global r 
    r = r + dr
    y = u(nmax,r)
    line.set_data(x, y)
    return line,
    
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, blit=True, interval=30, repeat=False)

plt.show()
