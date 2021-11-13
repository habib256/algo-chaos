"""
=====
Algo & Chaos 3
PendulePhaseSpace.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

"""
import matplotlib.pyplot as plt
from numpy import cos, sin, pi, linspace
from scipy.integrate import solve_ivp

# ----------
# CONSTANTES 

OMEGA = 2*pi
OMEGA0 = 1.5*OMEGA
BETA = OMEGA0/4
GAMMA = 1.0569

# ---------
# FONCTIONS

def fun(t,x):
    phi,phipoint = x[0], x[1]
    v = phipoint
    phipointpoint = -2*BETA*phipoint - OMEGA0**2*sin(phi) + GAMMA*OMEGA0**2*cos(OMEGA*t)
    return phipoint,phipointpoint

t_max = 50
N_pas = 10000
y0 = [0,0]
sol = solve_ivp(fun, [0,t_max],[0,0], t_eval=linspace(0., t_max, N_pas), rtol=1e-9)

fig, ax = plt.subplots()
plt.plot(sol.y[0],sol.y[1], linewidth=1)
plt.scatter(0,0, marker='+',s=200,c='black')
plt.xticks((0,2*pi,4*pi),("0",r"$2\pi$",r"$4\pi$"))
plt.show()