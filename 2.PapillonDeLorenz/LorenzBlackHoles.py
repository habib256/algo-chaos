"""
=====
Algo & Chaos 2
LorenzBlackHoles.py
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

X0 = 0.
EPSILON = 0.01
Y0 = 1.
Z0 = 3.
DT = 0.01
NBPASMAX = 10000

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

pos=np.zeros((3,NBPASMAX))

# GENERER LES DATAS (POINTS DE LA TRAJECTOIRE DE LORENZ)
pos_gen = iter(lorenz_gen(X0,Y0,Z0,DT))
for i in range(0,NBPASMAX) :
    pos[0][i],pos[1][i],pos[2][i] = next(pos_gen)

# ANIMATION FUNCTION
def func(num, dataSet, line):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(pos[0:2, :num])    
    line.set_3d_properties(pos[2, :num])
    #ax.scatter(pos[0][num], pos [1][num], pos[2][num])
    ax.view_init(15, num/2)
    return line
  
# GET SOME MATPLOTLIB OBJECTS
fig = plt.figure()
ax = plt.axes(projection='3d')

# AXES PROPERTIES]
ax.set_axis_off()
ax.set_title('Lorenz "Black Holes"')
 
# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(pos[0], pos[1], pos[2], lw=0.5, c='r')[0] # For line plot
 
# Creating the Animation object
line_ani = animation.FuncAnimation(fig, func, frames=NBPASMAX, fargs=(pos,line), interval=50, blit=False)
#line_ani.save(r'AnimationNew.mp4')

plt.show()