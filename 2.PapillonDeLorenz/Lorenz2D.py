"""
=====
Algo & Chaos 2
LorenzModel.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Implémentation basique du modèle de Lorenz basée sur la publication 
d'Edward Lorenz de 1963 : "Deterministic Nonperiodic Flow".
https://raw.githubusercontent.com/habib256/algo-chaos/main/2.PapillonDeLorenz/docs/%5BEdward%20N%20Lorenz%20-%20Journal%20of%20the%20Atmospheric%20Sciences%5D%20Deterministic%20Nonperiodic%20Flow.pdf

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ----------
# CONSTANTES

AXE_COLOR = 'lightgoldenrodyellow'
TITLE = "Lorenz "+"$u_{n+1} =r.u_n (1-u_n)$"

dt = 0.01
NbPasMax = 10000

# Valeur maximale + 1 car il y a les valeurs initiales
xs = np.empty((NbPasMax + 1,))
ys = np.empty((NbPasMax + 1,))
zs = np.empty((NbPasMax + 1,))

# Affecter les valeurs initiales
xs[0], ys[0], zs[0] = (0., 1., 3.)

# ---------
# FONCTIONS

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_point = s*(y - x)
    y_point = r*x - y - x*z
    z_point = x*y - b*z
    return x_point, y_point, z_point

def termes_u(n, r, u0):
    """Calcul des n premiers termes de la suite"""
    termes = [u0]
    for i in range(n):
        u = termes[-1]
        termes.append(f(r,u))
    return termes

def update(i):
    """La fonction de rafraichissement de la courbe"""
    # on efface juste ce qu'il faut... le ax.clear() efface trop de choses
    for l in ax.lines:
        l.remove()
    #ax.plot(termes_u(NMAX, r_slider.val, u0_slider.val), 'bo')


# -------------------
# PROGRAMME PRINCIPAL

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

# --- Les 2 sliders

axr = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=AXE_COLOR)
r_slider = Slider(
    ax=axr,
    label='Croissance r',
    valmin=0.1,
    valmax=4,
    valinit=xs[0],
)

axu0 = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=AXE_COLOR)
u0_slider = Slider(
    ax=axu0,
    label="$u_0$",
    valmin=0,
    valmax=1,
    valinit=ys[0],
    orientation="vertical"
)

# --- Elements figés du graphique

ax.set_xlabel('n')
ax.set_ylabel("$u_n$")
ax.set_ylim(0,1)
ax.margins(x=0)
ax.set_title(TITLE)


# --- Connecte les évènements des Sliders à la fonction update()
# --- Lorsqu'un Slider est modifié update Recalcule la suite
r_slider.on_changed(update)
u0_slider.on_changed(update)

# --- Dessine une première fois la courbe et affiche la courbe pltplot!
update(0)
plt.show()