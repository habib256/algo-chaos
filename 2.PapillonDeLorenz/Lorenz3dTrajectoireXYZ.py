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
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# ----------
# CONSTANTES 

X0 = 0.
EPSILONX = 0.01
Y0 = 1.
Z0 = 3.
DT = 0.01

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

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
        #yield np.array(x, y, z)
        # On applique les équations de Lorenz
        x_point, y_point, z_point = lorenz(x,y,z)
        # Et on calcule l'état suivant pour X, Y, Z grâce à EULER
        x = x + x_point * dt
        y = y + y_point * dt
        z = z + z_point * dt

def update(num, line):
    line.set_data(x,y,z)
   # line.set_3d_properties(data[2, :num])

Objet1position = iter(lorenz_gen(X0,Y0,Z0,DT))
line, = ax.plot(X0, Y0, Z0)

# Setting the axes properties
ax.set_xlim3d([-30.0, 30.0])
ax.set_xlabel('X')

ax.set_ylim3d([-30.0, 30.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-30.0, 30.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, fargs=( line,), interval=15, blit=False)
#ani.save('matplot003.gif', writer='imagemagick')
plt.show()
