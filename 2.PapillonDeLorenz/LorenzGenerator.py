"""
=====
Algo & Chaos 2
LorenzGenerator.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Implémentation basique du modèle de Lorenz basée sur la publication 
d'Edward Lorenz de 1963 : "Deterministic Nonperiodic Flow".
https://raw.githubusercontent.com/habib256/algo-chaos/main/2.PapillonDeLorenz/%5BEdward%20N%20Lorenz%20-%20Journal%20of%20the%20Atmospheric%20Sciences%5D%20Deterministic%20Nonperiodic%20Flow.pdf

"""

X0 = 0.
Y0 = 1.
Z0 = 3.

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_point = s*(y - x)
    y_point = r*x - y - x*z
    z_point = x*y - b*z
    return x_point, y_point, z_point

def lorenz_gen(x0, y0, z0):
    x=x0
    y=y0
    z=z0
    dt = 0.01
    while (True) :
        # On applique les équations de Lorenz
        x_point, y_point, z_point = lorenz(x,y,z)
        # On calcule l'état suivant pour X, Y, Z grâce à EULER
        x = x + x_point * dt
        y = y + y_point * dt
        z = z + z_point * dt
        # Générateur donc stop jusqu'au prochain next
        yield x,y,z

position = iter(lorenz_gen(X0,Y0,Z0))

for i in range(0,20) :
    print(next(position))

