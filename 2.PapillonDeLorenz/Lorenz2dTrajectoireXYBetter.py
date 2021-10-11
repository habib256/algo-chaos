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
matplotlib.use('Qt4Agg'))

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

x1s=[]
y1s=[]
z1s=[]
x2s=[]
y2s=[]
z2s=[]

Objet1position = iter(lorenz_gen(X0,Y0,Z0,DT))
Objet2position = iter(lorenz_gen(X0+EPSILONX,Y0,Z0,DT))

px = 1/plt.rcParams['figure.dpi']  # pixel in inches

fig, ax = plt.subplots(figsize=(580*px, 380*px))

ax = plt.axis([-25,30,-30,30])
ax = plt.title("Trajectoires de Lorenz XY: Papillon en 2D")
ax = plt.xlabel("X")
ax = plt.ylabel("Y")

x1s.append(X0)
y1s.append(Y0)
x2s.append(X0+EPSILONX)
y2s.append(Y0)

trajectoireRouge, = plt.plot(x1s, y1s, 'r-')
trajectoireBleu, = plt.plot(x2s, y2s, 'b-')
pointRouge, = plt.plot(X0, Y0, 'ro')
pointBleu, = plt.plot(X0+EPSILONX, Y0, 'bo')

def animate(frame):
    x1,y1,z1 = next(Objet1position)
    x2,y2,z2 = next(Objet2position)
    x1s.append(x1)
    y1s.append(y1)
    x2s.append(x2)
    y2s.append(y2)

    trajectoireRouge.set_data(x1s,y1s)
    trajectoireBleu.set_data(x2s,y2s)
    pointRouge.set_data(x1,y1)
    pointBleu.set_data(x2,y2)
   
    return trajectoireRouge, trajectoireBleu, pointRouge, pointBleu, 

# créer une animation en utilisant la fonction animate()
myAnimation = animation.FuncAnimation(fig, animate, frames=1000, \
                                      interval=30, blit=True, repeat=True)
#myAnimation.save('Lorenz2DXY.gif', writer='imagemagick')
#gifsicle -b -O2 --colors 16 Lorenz2DXY.gif

plt.show()
