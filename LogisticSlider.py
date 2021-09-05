import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

nmax = 40
r = 2.4
u0 = 0.7

def u(n):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

fig, ax = plt.subplots()
ax.set_xlabel('n')
ax.set_ylabel("$u_n$")
axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)
plt.subplots_adjust(left=0.25, bottom=0.25)

title ="Suite logistique "+"$u_{n+1} =r.u_n (1-u_n)$"
ax.set_title(title)

axr = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
r_slider = Slider(
    ax=axr,
    label='Croissance r',
    valmin=0.1,
    valmax=4,
    valinit=r,
)
axu0 = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=axcolor)
u0_slider = Slider(
    ax=axu0,
    label="$u_0$",
    valmin=0,
    valmax=1,
    valinit=u0,
    orientation="vertical"
)

# The function to be called anytime a slider's value changes
def update(val):
    #line.set_ydata(f(t, u0_slider.val, r_slider.val))
    fig.canvas.draw_idle()

ax.plot([u(k) for k in range(nmax)],'bo')


plt.show()