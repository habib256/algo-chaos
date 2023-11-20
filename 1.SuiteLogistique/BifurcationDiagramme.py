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

import matplotlib.pyplot as plt


nmin = 40     # Valeur minimale de n 
nmax = 200    # Valeur maximale de n
r = 1.0       # Le taux de croissance de départ
rmax = 4.0    # Le taux de croissance maximal
dr = 0.001   # La variation de r soit la capacité à zoomer dans le diagramme
u0 = 0.6      # La population initiale en %

# C'est la suite Un définie itérativement
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

# C'est ici qu'on calcule les valeurs du diagramme de bifurcation
x = []
y = []
while r < rmax :
    for n in range (nmin ,nmax) :
        x.append(float(r))
        y.append(float(u(n,r,u0)))
    r=r+dr

plt.scatter(x,y,1)

# On affiche la fenêtre pltplot
plt.show()