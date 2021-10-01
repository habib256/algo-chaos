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
import matplotlib.animation as animation

# ----------
# CONSTANTES 

X0 = 0.
EPSILONX = 0.0001
Y0 = 1.
Z0 = 3.
DT = 0.01
NbPasMax = 10000

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

fig, ax = plt.subplots()

ax = plt.axis([-20,20,-30,60])

x1s.append(X0)
y1s.append(Y0)
z1s.append(Z0)
x2s.append(X0+EPSILONX)
y2s.append(Y0)
z2s.append(Z0)

redDot, = plt.plot(x1s, y1s, 'ro')
blueDot, = plt.plot(x1s, z1s, 'bo')
greenDot, = plt.plot(y1s, z1s, 'go')

def animate(t):
    x1,y1,z1 = next(Objet1position)
    x2,y2,z2 = next(Objet2position)
    x1s.append(x1)
    y1s.append(y1)
    z1s.append(z1)
    x2s.append(x2)
    y2s.append(y2)
    z2s.append(z2)

    redDot.set_data(x1s,y1s)
    blueDot.set_data(x2s,y2s)

    #greenDot.set_data(y1s,z1s)
   
    return redDot, blueDot, greenDot, 

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, NbPasMax*DT, DT), \
                                      interval=1, blit=True, repeat=True)

plt.show()
