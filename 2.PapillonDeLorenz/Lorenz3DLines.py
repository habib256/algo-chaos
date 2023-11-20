"""
=====
Algo & Chaos 2
Lorenz3DLines.py
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

# ----------
# CONSTANTES 

EPSILON = 0.01
DT = 0.001
NBPASMAX = 1000
OBJETMAX = 48

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

# -------------------
# PROGRAMME PRINCIPAL

pos=np.zeros((OBJETMAX,3,NBPASMAX))

# GENERER LES DATAS (POINTS DE LA TRAJECTOIRE DE LORENZ)
objectNb = 0
for i in range(-20,20,11):
    for j in range(-20,20,11):
        for k in range(0,20,8):
            pos_gen = iter(lorenz_gen(i,j,k,DT))
            for l in range(0,NBPASMAX) :
                pos[objectNb][0][l],pos[objectNb][1][l],pos[objectNb][2][l] = next(pos_gen)
            objectNb = objectNb + 1

print(str(objectNb)+ " objets présents")

# FONNCTION D'ANIMATION
def func(num, dataSet, line):
    ax.clear()
    ax.set_axis_off()
    for i in range (0, OBJETMAX) :
        ax.scatter(pos[i][0][:num], pos[i][1][:num], pos[i][2][:num],alpha=0.25, s=0.05)   
    ax.view_init(15, num/2)
    return line
  
# GET SOME MATPLOTLIB OBJECTS
fig = plt.figure()
ax = plt.axes(projection='3d')

# AXES PROPERTIES]
ax.set_axis_off()
ax.set_title('Lorenz 3D Line')
 
# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(pos[0][0], pos[0][1], pos[0][2], lw=0.5, c='r')[0] # For line plot
 
# Creating the Animation object
monanim = animation.FuncAnimation(fig, func, frames=NBPASMAX, fargs=(pos,line), interval=30, blit=False)
#monanim.save(r'AnimationNew.mp4')

plt.show()