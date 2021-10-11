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

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ----------
# CONSTANTES 

X0 = 0.
EPSILONX = 0.01
Y0 = 1.
Z0 = 3.
DT = 0.01

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

trajectoire1 = [[X0],[Y0],[Z0]]
trajectoire2 = [[X0+EPSILONX],[Y0],[Z0]]

Objet1position = iter(lorenz_gen(X0,Y0,Z0,DT))
Objet2position = iter(lorenz_gen(X0+EPSILONX,Y0,Z0,DT))

fig, ax = plt.subplots()

ax = plt.axis([-25,30,-30,30])
ax = plt.title("Trajectoires de Lorenz XY: Papillon en 2D")
ax = plt.xlabel("X")
ax = plt.ylabel("Y")

trajectoireRouge, = plt.plot(trajectoire1[0],trajectoire1[1], 'r-')
trajectoireBleu, = plt.plot(trajectoire2[0],trajectoire2[1], 'b-')
pointRouge, = plt.plot(X0, Y0, 'ro')
pointBleu, = plt.plot(X0+EPSILONX, Y0, 'bo')

def animate(i):
    x1,y1,z1 = next(Objet1position)
    x2,y2,z2 = next(Objet2position)
    trajectoire1[0].append(x1)
    trajectoire1[1].append(y1)
    trajectoire1[2].append(z1)
    trajectoire2[0].append(x2)
    trajectoire2[1].append(y2)
    trajectoire2[2].append(z2)

    trajectoireRouge.set_data(trajectoire1[0],trajectoire1[1])
    trajectoireBleu.set_data(trajectoire2[0],trajectoire2[1])
    pointRouge.set_data(x1,y1)
    pointBleu.set_data(x2,y2)
   
    return trajectoireRouge, trajectoireBleu, pointRouge, pointBleu, 

# créer une animation en utilisant la fonction animate()
myAnimation = animation.FuncAnimation(fig, animate, frames=1300, \
                                      interval=15, blit=True, repeat=True)
#myAnimation.save('Lorenz2DXY.gif', writer='imagemagick')
#gifsicle -b -O2 --colors 16 Lorenz2DXY.gif

plt.show()
