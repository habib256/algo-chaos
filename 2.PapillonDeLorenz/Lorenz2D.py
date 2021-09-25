"""
=====
Algo & Chaos 2
LorenzGenerator.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Implémentation basique du modèle de Lorenz basée sur la publication 
d'Edward Lorenz de 1963 : "Deterministic Nonperiodic Flow".
https://raw.githubusercontent.com/habib256/algo-chaos/main/2.PapillonDeLorenz/docs/%5BEdward%20N%20Lorenz%20-%20Journal%20of%20the%20Atmospheric%20Sciences%5D%20Deterministic%20Nonperiodic%20Flow.pdf

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------
# CONSTANTES 

X0 = 0.
Y0 = 1.
Z0 = 3.

DT = 0.01
NbPasMax = 10000

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

    t = 0.0
    ts=[]
    xs=[]
    ys=[]
    zs=[]

fig, ax = plt.subplots()
line = plt.plot([0.0],[X0],'r+',[], [],'bo-')

position = iter(lorenz_gen(X0,Y0,Z0,DT))

def init():
    line[1].set_data([], [])
    return (line)

def update(frame):
    x,y,z = next(position)
    ts.append(t)
    t = t + DT
    xs.append(x)
    ys.append(y)
    zs.append(z)
    line.set_data(xs,ys)
    print(next(position))
    return ln, 

anim = FuncAnimation(fig, update, frames=100000,interval=30,
                    init_func=init, blit=True)
anim
