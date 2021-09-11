"""
=====
Algo & Chaos 1
BifurcationDiagramme.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Représentation du diagramme de bifurcation de
la suite logistique u = r*u(1-u)

"""
import numpy as np
import matplotlib.pyplot as plt


nmin = 30   # Valeur minimale de n pour parfois obtenir une convergence
nmax = 200  # Valeur maximale de n
r = 0       # Le taux de croissance
u0 = 0.6    # La population initiale en % n'a quasiment pas d'influence

# C'est la suite Un définie récursivement
def u(n,r,u0):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

# Il est possible de s'inspirer des Formules LaTeX sous matplotlib pour générer de belles formules
title ="Diagramme de bifurcation de "+"$u_{n+1} = r.u_n (1-u_n)$"
plt.title(title)
plt.xlabel("r")
plt.ylabel("Valeurs de "+"$u_n$")

# C'est ici qu'on calcule les valeurs ddu diagramme de bifurcation
x = []
y = []
for i in range (4000 , 16000) :
    r = float(i/4000.0)
    for n in range (nmin ,nmax) :
        x.append(float(r))
        y.append(float(u(n,r,u0)))

plt.scatter(x,y,1)

# On affiche la fenêtre pltplot
plt.show()