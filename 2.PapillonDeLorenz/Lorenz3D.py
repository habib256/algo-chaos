"""
=====
Algo & Chaos 2
Lorenz3D.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Implémentation basique du modèle de Lorenz basée sur la publication 
d'Edward Lorenz de 1963 : "Deterministic Nonperiodic Flow".
https://raw.githubusercontent.com/habib256/algo-chaos/main/2.PapillonDeLorenz/docs/%5BEdward%20N%20Lorenz%20-%20Journal%20of%20the%20Atmospheric%20Sciences%5D%20Deterministic%20Nonperiodic%20Flow.pdf

"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

NbPasMax = 10000

X0 = 0.
Y0 = 1.
Z0 = 3.

# ---------
# FONCTIONS

def lorenz(x, y, z, s=10, r=28, b=2.667):
    """Calcul des dérivées de Lorenz par rapport au temps"""
    x_point = s*(y - x)
    y_point = r*x - y - x*z
    z_point = x*y - b*z
    return x_point, y_point, z_point

def lorenz_gen(x0, y0, z0):
    """Un générateur Python des états successifs de Lorenz"""
    x=x0
    y=y0
    z=z0
    dt = 0.01
    while (True) :
        # C'est un générateur Python donc 
        # il stoppe après yield et reprends au prochain appel via next
        yield x,y,z
        # On applique les équations de Lorenz
        x_point, y_point, z_point = lorenz(x,y,z)
        # Et on calcule l'état suivant pour X, Y, Z grâce à EULER
        x = x + x_point * dt
        y = y + y_point * dt
        z = z + z_point * dt

# -------------------
# PROGRAMME PRINCIPAL

xs=[]
ys=[]
zs=[]

position = iter(lorenz_gen(X0,Y0,Z0))

for i in range(0,NbPasMax) :
    x,y,z = next(position)
    xs.append(x)
    ys.append(y)
    zs.append(z)

fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = plt.axes(projection='3d')

ax.set_xlabel("Axes des X")
ax.set_ylabel("Axes des Y")
ax.set_zlabel("Axes des Z")
ax.set_title("Attracteurs étranges du Papillon de Lorenz")

ax.plot(xs, ys, zs, lw=0.5)

plt.show()
