"""
=====
Algo & Chaos 2
Lorenz2dAnim.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Implémentation basique du modèle de Lorenz basée sur la publication 
d'Edward Lorenz de 1963 : "Deterministic Nonperiodic Flow".
https://raw.githubusercontent.com/habib256/algo-chaos/main/2.PapillonDeLorenz/docs/%5BEdward%20N%20Lorenz%20-%20Journal%20of%20the%20Atmospheric%20Sciences%5D%20Deterministic%20Nonperiodic%20Flow.pdf

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ----------
# CONSTANTES 

X0 = 0.
Y0 = 1.
Z0 = 3.
DT = 0.01
NbPasMax = 1000

# ---------
# FONCTIONS

def lorenz(x, y, z, s=10, r=28, b=2.667):
    """Calcul des dérivées de Lorenz par rapport au temps"""
    x_point = s*(y - x)
    y_point = r*x - y - x*z
    z_point = x*y - b*z
    return x_point, y_point, z_point

def lorenz_gen(x0, y0, z0, dt):
    """Un générateur Python des états successifs de Lorenz"""
    x=x0
    y=y0
    z=z0
    while (True) :
        # C'est un générateur Python donc il stoppe après yield 
        # et il ne reprendra qu'au prochain appel via next
        yield x,y,z
        # On applique les équations de Lorenz
        x_point, y_point, z_point = lorenz(x,y,z)
        # Et on calcule l'état suivant pour X, Y, Z grâce à EULER
        x = x + x_point * dt
        y = y + y_point * dt
        z = z + z_point * dt

# -------------------
# PROGRAMME PRINCIPAL

position = iter(lorenz_gen(X0,Y0,Z0,DT))

fig, ax = plt.subplots()

ax = plt.axis([0,NbPasMax*DT,-30,60])

redDot, = plt.plot([0], [X0], 'ro')
blueDot, = plt.plot([0], [Y0], 'bo')
greenDot, = plt.plot([0], [Z0], 'go')

def animate(t):
    x,y,z = next(position)
    redDot.set_data(t, x)
    blueDot.set_data(t, y)
    greenDot.set_data(t, z)
    return redDot, blueDot, greenDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, NbPasMax*DT, DT), \
                                      interval=30, blit=True, repeat=True)

plt.show()
