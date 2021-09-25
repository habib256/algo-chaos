import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def ts_anim():
    # create a simple animation
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 100), ylim=(-1, 1))
    Color = [ 1 ,0.498039, 0.313725]
    line, = ax.plot([], [], 'o',color = Color)
    plt.xlabel("Time")
    plt.ylabel("Measurement")

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x = np.linspace(0, i+1, i+1)
        ts = 5*np.cos(x * 0.002 * np.pi) * np.sin(np.cos(x)  * 0.002 * np.pi)
        line.set_data(x, ts)
        return line,

    return animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=100, interval=200, blit=True) 
           
myanim = ts_anim()

plt.show()