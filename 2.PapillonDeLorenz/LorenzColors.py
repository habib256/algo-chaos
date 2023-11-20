"""
=====
Algo & Chaos 2
LorenzColors.py

A lancer à partir d'un shell pour profiter de end='\r'
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
from mpl_toolkits.mplot3d import Axes3D
import numba

# Constantes
DT = 0.008
EPSILON = 0.00001
NBPASMAX = 2000
OBJETMAX = 10000

# Fonctions
@numba.jit(nopython=True)
def lorenz(x, y, z, s=10, r=28, b=2.667):
    """Calcul des dérivées de Lorenz par rapport au temps"""
    x_point = s*(y - x)
    y_point = r*x - y - x*z
    z_point = x*y - b*z
    return x_point, y_point, z_point

@numba.jit(nopython=True)
def lorenz_gen(x0, y0, z0, dt):
    """Un générateur Python des états successifs de Lorenz"""
    x, y, z = x0, y0, z0
    while True:
        yield x, y, z
        x_point, y_point, z_point = lorenz(x, y, z)
        x += x_point * dt
        y += y_point * dt
        z += z_point * dt

# Programme principal
pos = np.zeros((OBJETMAX, 3, NBPASMAX))

# Générer les datas
print(f"L'ordinateur calcule {OBJETMAX} trajectoires. Patientez svp...")
objectNb = 0
for i in np.arange(-1.0, 1.0, EPSILON):
    if objectNb >= OBJETMAX:
        break
    for j in np.arange(0.0, 2.0, EPSILON):
        if objectNb >= OBJETMAX:
            break
        for k in np.arange(2.0, 4.0, EPSILON):
            if objectNb >= OBJETMAX:
                break
            pos_gen = iter(lorenz_gen(i, j, k, DT))
            pos[objectNb] = np.array([next(pos_gen) for _ in range(NBPASMAX)]).T
            objectNb += 1

print(f"\nIl y a exactement {objectNb} trajectoires à calculer.")

# Fonction d'animation
def update(num):
    ax.clear()
    ax.set_axis_off()
    ax.set_xlim3d(-30, 30)
    ax.set_ylim3d(-30, 30)
    ax.set_zlim3d(0, 50)

    xs, ys, zs = pos[:objectNb, :, num].transpose()
    colors = np.arange(objectNb)
        
    cmap = plt.cm.viridis
    ax.scatter(xs, ys, zs, alpha=0.5, s=2, c=cmap(colors))
    ax.view_init(0, 160)

# Récupérer les objets matplotlib
fig = plt.figure()
ax = plt.axes(projection='3d')

# On efface les axes
ax.set_axis_off()

# Création d'un objet Animation
monanim = animation.FuncAnimation(fig, update, frames=NBPASMAX-1, interval=1000/30, blit=False)
#monanim.save(r'AnimationNew.mp4')
plt.show()
