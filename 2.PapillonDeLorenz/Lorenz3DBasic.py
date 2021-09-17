"""
=====
Algo & Chaos 2
LorenzModel.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Implémentation basique du modèle de Lorenz basée sur la publication 
d'Edward Lorenz de 1963 : "Deterministic Nonperiodic Flow".
https://raw.githubusercontent.com/habib256/algo-chaos/main/2.PapillonDeLorenz/%5BEdward%20N%20Lorenz%20-%20Journal%20of%20the%20Atmospheric%20Sciences%5D%20Deterministic%20Nonperiodic%20Flow.pdf

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_point = s*(y - x)
    y_point = r*x - y - x*z
    z_point = x*y - b*z
    return x_point, y_point, z_point


dt = 0.01
NbPasMax = 10000

# valeurs initiales + 1
xs = np.empty((NbPasMax + 1,))
ys = np.empty((NbPasMax + 1,))
zs = np.empty((NbPasMax + 1,))

# Affecter les valeurs initiales
xs[0], ys[0], zs[0] = (0., 1., 3.)

# On avance dans le temps 
for i in range(NbPasMax):
    # On dérive l'état X, Y, Z grâce à EULER
    x_point, y_point, z_point = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_point * dt)
    ys[i + 1] = ys[i] + (y_point * dt)
    zs[i + 1] = zs[i] + (z_point * dt)

fig = plt.figure()
ax = fig.gca(projection='3d')


ax.set_xlabel("Axes des X")
ax.set_ylabel("Axes des Y")
ax.set_zlabel("Axes des Z")
ax.set_title("Attracteur étrange de Lorenz")

ax.plot(xs, ys, zs, lw=0.5)

plt.show()