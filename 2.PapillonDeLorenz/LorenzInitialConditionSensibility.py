"""
=====
Algo & Chaos 2
LorenzInitialConditionSensibility.py

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

# ----------
# CONSTANTES 

DT = 0.008
EPSILON = 0.000015
NBPASMAX = 2000
OBJETMAX = 133334
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

# GENERER LES DATAS (GRILLES DE POINTS POUR LES TRAJECTOIRES DE LORENZ)
print ("L'ordinateur calcule "+str(OBJETMAX)+" trajectoires. Patientez svp...")
objectNb = 0
i = -1.0
j = 0.0
k = 2.0
while i < 1.0 :
    i = i+ EPSILON
    while j < 2.0 :
        j = j+ EPSILON
        while k < 4.0 :
            k = k+ EPSILON
            pos_gen = iter(lorenz_gen(i,j,k,DT))
            for l in range(0,NBPASMAX) :
                pos[objectNb][0][l],pos[objectNb][1][l],pos[objectNb][2][l] = next(pos_gen)
            objectNb = objectNb + 1
            print ("  ["+str(objectNb)+ " / "+str(OBJETMAX)+"]", end='\r')

print("\nIl y a exactement " + str(objectNb)+ " trajectoires à calculer.")

# FONCTION D'ANIMATION
def update(num):
    ax.clear()
    ax.set_axis_off()
    ax.set_xlim3d(-30, 30)
    ax.set_ylim3d(-30, 30)
    ax.set_zlim3d(0, 50)

    xs= []
    ys= []
    zs= []
    for i in range (0, objectNb) :
        xs.append(pos[i][0][num])
        ys.append(pos[i][1][num])
        zs.append(pos[i][2][num])

    ax.scatter(xs, ys, zs,alpha=0.1, s=0.5)

    ax.view_init(0,180)    #Vue fabuleuse pour projection 2D !

    print ("  Avancement du calcul de l'animation : [" + str(num) + " /"+ str(NBPASMAX)+"] images", end="\r")
  
# On récupère les objets matplotlib
fig = plt.figure(dpi=250)
ax = plt.axes(projection='3d')

# On efface les axes
ax.set_axis_off()
# On supprime le cadre blanc
fig.subplots_adjust(bottom = 0)
fig.subplots_adjust(top = 1)
fig.subplots_adjust(right = 1)
fig.subplots_adjust(left = 0)

# Création d'un objet Animation
monanim = animation.FuncAnimation(fig, update, frames=NBPASMAX-1, interval=20, blit=False)

monanim.save(r'AnimationNew.mp4')

#plt.show()