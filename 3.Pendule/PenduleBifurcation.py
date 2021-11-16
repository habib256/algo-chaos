"""
=====
Algo & Chaos 3
PenduleBifurcation.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

omega = 2*np.pi      #
omega0 = 1.5*omega   # paramètres proposés par Taylor
beta = omega0/4      #

def fun(t, x):
    phi, phipoint = x[0], x[1]
    v = phipoint
    a = -2*beta*phipoint - omega0**2*np.sin(phi) + gamma*omega0**2*np.cos(omega*t)
    return v, a

t_max = 61          # fin de l'intégration
N_pas = 1000        # nb de pas
N_points = 10       # nb de points affichés à chaque valeur de gamma
t = np.arange(t_max - N_points, t_max)
liste_gamma = np.arange(1.0, 1.1, 0.0002)
thetas, gammas = [], []
y0=[0,0]
for i, gamma in enumerate(liste_gamma):
    sol = solve_ivp(fun, [0, t_max], y0, t_eval=np.linspace(0., t_max, N_pas), rtol=1e-9, dense_output=True)
    gammas += [gamma] * N_points
    thetas += list((sol.sol(t)[0]+np.pi)%(2*np.pi)-np.pi)
    print("gamma=%.6f [%d/%d]" % (gamma, i+1, len(liste_gamma)), end="\r")
    y0=sol.sol(t_max)  # initialisation pour le prochain calcul
plt.scatter(gammas, thetas, c='black', s=1)
plt.ylim(-1.5, 0)
plt.show()