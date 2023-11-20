"""
=====
Algo & Chaos 2
Lorenz2dTrajectoireXY.py
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

# CONSTANTES 
X0, Y0, Z0, DT, EPSILONX = 0., 1., 3., 0.01, 0.01

# FONCTIONS
def lorenz(x, y, z, s=10, r=28, b=2.667):
    """Calcul des dérivées de Lorenz par rapport au temps"""
    return s*(y - x), r*x - y - x*z, x*y - b*z

def lorenz_gen(x0, y0, z0, dt):
    """Un générateur Python des états successifs de Lorenz"""
    x, y, z = x0, y0, z0
    while True:
        yield x, y, z
        x_point, y_point, z_point = lorenz(x, y, z)
        x += x_point * dt
        y += y_point * dt
        z += z_point * dt

# PROGRAMME PRINCIPAL
Objet1position = iter(lorenz_gen(X0, Y0, Z0, DT))
Objet2position = iter(lorenz_gen(X0+EPSILONX, Y0, Z0, DT))

fig, ax = plt.subplots()
ax.axis([-25,30,-30,30])
ax.set_title("Trajectoires de Lorenz XY: Papillon en 2D")
ax.set_xlabel("X")
ax.set_ylabel("Y")

x1s, y1s = [X0], [Y0]
x2s, y2s = [X0+EPSILONX], [Y0]

trajectoireRouge, = plt.plot(x1s, y1s, 'r-')
trajectoireBleu, = plt.plot(x2s, y2s, 'b-')
pointRouge, = plt.plot(X0, Y0, 'ro')
pointBleu, = plt.plot(X0+EPSILONX, Y0, 'bo')

def animate(frame):
    temp_x1s, temp_y1s, temp_x2s, temp_y2s = [], [], [], []
    for _ in range(2):  # Adjust this value as needed
        x1, y1, z1 = next(Objet1position)
        x2, y2, z2 = next(Objet2position)
        temp_x1s.append(x1)
        temp_y1s.append(y1)
        temp_x2s.append(x2)
        temp_y2s.append(y2)

    x1s.extend(temp_x1s)
    y1s.extend(temp_y1s)
    x2s.extend(temp_x2s)
    y2s.extend(temp_y2s)

    trajectoireRouge.set_data(x1s, y1s)
    trajectoireBleu.set_data(x2s, y2s)
    pointRouge.set_data([x1], [y1])
    pointBleu.set_data([x2], [y2])

    return trajectoireRouge, trajectoireBleu, pointRouge, pointBleu,

myAnimation = animation.FuncAnimation(fig, animate, frames=1300, interval=1000/30, blit=True, repeat=True)

plt.show()
