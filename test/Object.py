import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Suite:
    def __init__(self):
        self.u0 = 0.6
        self.r = 3.4

    def u(self, x):
        u = self.u0
        for n in range(x):
            u=self.r*u*(1-u)
        return u

    def _set_r(self,v):
        self.r = v

    def _get_r(self):
        return self.r


def animate(s):
    xs = []
    ys = []
    for n in range (0 ,30, 1) :
        xs.append(float(n))
        ys.append(float(s.u(n)))
    ax1.clear()
    ax1.plot(xs, ys)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

s = Suite()

ani = animation.FuncAnimation(fig, animate(s), interval=30)
plt.show()

