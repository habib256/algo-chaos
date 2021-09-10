"""
=====
Algo & Chaos 1
LogistiqueBasic.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Représentation simple de 
la suite logistique u = r*u(1-u)

"""

import matplotlib.pyplot as plt

nmax = 60   # C'est l'année calculée maximale
r = 2.7     # C'est le taux de croissance
u0 = 0.7    # C'est la population initiale en %

# C'est la suite Un définie récursivement
def u(n):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

# Il est possible de s'inspirer des Formules LaTeX sous matplotlib pour générer de belles formules
title ="Suite logistique "+"$u_{n+1} ="+str(r)+"u_n (1-u_n)$"+" avec "+"$u_0 ="+str(u0)+"$"
plt.title(title)
plt.xlabel("n")
plt.ylabel("$u_n$")

# C'est ici qu'on calcule les valeurs de la suite
plt.plot([u(k) for k in range(nmax)],'bo')

# On affiche la fenêtre pltplot
plt.show()