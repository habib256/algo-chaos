"""
=====
Algo & Chaos 1
SuiteLogistiqueSimple.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

Représentation simple de 
la suite logistique u = r*u(1-u)

"""

import matplotlib.pyplot as plt

NMAX = 60   # C'est l'année calculée maximale
R = 3.84     # C'est le taux de croissance
UO = 0.7    # C'est la population initiale en %

def u(n):
    """ C'est la suite Un définie itérativement """
    u=UO
    for i in range(n):
        u=R*u*(1-u)
    return u

# Il est possible de s'inspirer des Formules LaTeX sous matplotlib pour générer de belles formules
title ="Suite logistique "+"$u_{n+1} ="+str(R)+"u_n (1-u_n)$"+" avec "+"$u_0 ="+str(UO)+"$"
plt.title(title)
plt.xlabel("n")
plt.ylabel("$u_n$")

# C'est ici qu'on calcule les valeurs de la suite
x = []
y = []
for n in range (0 ,NMAX) :
    x.append(float(n))
    y.append(float(u(n)))

plt.plot(x,y,'bo')

# Methode plus rapide et compacte
# plt.plot([u(k) for k in range(NMAX)],'bo') 

# On affiche la fenêtre pltplot
plt.show()