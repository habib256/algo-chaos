"""
=====
LogistiqueSlider.py
=====

Représentation avec Sliders de 
la suite logistique u = r*u(1-u)

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Définition de la suite logistique
nmax = 80
r = 2.4
u0 = 0.7

def u(n,r,u0):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

# Construire les axes pour les sliders et le plot
fig, ax = plt.subplots()
axcolor = 'lightgoldenrodyellow'
plt.subplots_adjust(left=0.25, bottom=0.25)
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

# Lorsqu'un Slider est modifié
# Trace une nouvelle courbe
def update(val):
    ax.clear()
    ax.set_xlabel('n')
    ax.set_ylabel("$u_n$")
    ax.set_ylim(0,1)
    ax.margins(x=0)
    title ="Suite logistique "+"$u_{n+1} =r.u_n (1-u_n)$"
    ax.set_title(title)
    line, = ax.plot([u(k,r_slider.val,u0_slider.val) for k in range(nmax)], 'bo')

# Connecte les evenements des Sliders à la fonction update()
r_slider.on_changed(update)
u0_slider.on_changed(update)

update(0)
plt.show()