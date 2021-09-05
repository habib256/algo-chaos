import matplotlib.pyplot as plt
import matplotlib.animation as animation

nmax = 28
r = 2.4
u0 = 0.7

def u(n):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

def animate():
    xs = []
    ys = []
    for n in range (0 ,nmax, 1) :
        xs.append(float(n))
        ys.append(float(u(n)))
    ax1.clear()
    ax1.plot(xs, ys)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ani = animation.FuncAnimation(fig, animate(), interval=10)
plt.show()