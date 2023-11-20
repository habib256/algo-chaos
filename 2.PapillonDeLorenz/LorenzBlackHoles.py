"""
=====
Algo & Chaos 2
LorenzBlackHoles.py
=====
2023 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Implémentation basique du modèle de Lorenz basée sur la publication 
d'Edward Lorenz de 1963 : "Deterministic Nonperiodic Flow".
https://raw.githubusercontent.com/habib256/algo-chaos/main/2.PapillonDeLorenz/docs/%5BEdward%20N%20Lorenz%20-%20Journal%20of%20the%20Atmospheric%20Sciences%5D%20Deterministic%20Nonperiodic%20Flow.pdf

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

# ----------
# CONSTANTES 

DT = 0.0015
NBPASMAX = 500
OBJETMAX = 100000

# ---------
# FONCTIONS

def lorenz(t, xyz, s=10, r=28, b=2.667):
    """Calcul des dérivées de Lorenz par rapport au temps"""
    x, y, z = xyz
    x_point = s*(y - x)
    y_point = r*x - y - x*z
    z_point = x*y - b*z
    return [x_point, y_point, z_point]

# -------------------
# PROGRAMME PRINCIPAL

pos=np.zeros((OBJETMAX,3,NBPASMAX))

# GENERER LES DATAS (POINTS POUR LES TRAJECTOIRES DE LORENZ)
objectNb = 0
for i in np.arange(-50,50,5):
    for j in np.arange(-50,50,2):
        for k in np.arange(0,80,40):
            sol = solve_ivp(lorenz, [0, NBPASMAX*DT], [i, j, k], t_eval=np.arange(0, NBPASMAX*DT, DT))
            pos[objectNb,:,:] = sol.y
            objectNb += 1

print(f"{objectNb} objets présents")

# FONCTION D'ANIMATION
def update(num):
    ax.clear()
    ax.set_axis_off()
    ax.set_xlim3d(-30, 30)
    ax.set_ylim3d(-30, 30)
    ax.set_zlim3d(0, 50)

    xs, ys, zs = pos[:objectNb,:,num].T

    ax.scatter(xs, ys, zs,alpha=1, s=3)

    ax.view_init(0,num)  # Rotation autour de la figure sur l'axe xy
    #ax.view_init(0,180)    #Vue fabuleuse !
  
# GET SOME MATPLOTLIB OBJECTS
fig = plt.figure()
ax = plt.axes(projection='3d')

# AXES PROPERTIES]
ax.set_axis_off()

# Creating the Animation object
monanim = animation.FuncAnimation(fig, update, frames=NBPASMAX, interval=30, blit=False)
#monanim.save(r'AnimationNew.mp4')
#monanim.save('AnimationNew.gif', writer='imagemagick')

plt.show()