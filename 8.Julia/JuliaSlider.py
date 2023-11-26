"""
=====
Algo & Chaos 1
LogistiqueSlider.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
Refactoring et corrections : HOARAU Sebastien (seb@univ.re)
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Représentation avec Sliders de 
la suite logistique u = r*u(1-u)

"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ----------
# CONSTANTES

NMAX = 400
DEFAULT_R = 2.4
DEFAULT_U0 = 0.7
AXE_COLOR = 'lightgoldenrodyellow'
TITLE = "Suite logistique "+"$u_{n+1} =r.u_n (1-u_n)$"

# ---------
# FONCTIONS

def f(r, u):
    """Un+1 = f(Un)"""
    return r * u * (1-u)

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
    ax.plot(termes_u(NMAX, r_slider.val, u0_slider.val), 'bo')


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
    valinit=DEFAULT_R,
)

axu0 = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=AXE_COLOR)
u0_slider = Slider(
    ax=axu0,
    label="$u_0$",
    valmin=0,
    valmax=1,
    valinit=DEFAULT_U0,
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