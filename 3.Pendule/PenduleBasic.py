"""
=====
Algo & Chaos 3
PenduleBasic.py
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
GAMMA = 1.073

# ---------
# FONCTIONS

def fun(t,x):
    phi,phipoint = x[0], x[1]
    v = phipoint
    a = -2*BETA*phipoint - OMEGA0**2*sin(phi) + GAMMA*OMEGA0**2*cos(OMEGA*t)
    return v,a

t_max = 60
N_pas = 1000
y0 = [0,0]
sol = solve_ivp(fun, [0,t_max],y0, t_eval=linspace(0., t_max, N_pas), rtol=1e-9)

fig, ax = plt.subplots()
plt.plot(sol.t,sol.y[0], c='k')
ax.set_xlabel("le temps t")
ax.set_ylabel(r"l'angle $\phi$")
ax.set_yticks((0, 2*pi, 4*pi))
ax.set_yticklabels(("0",r"$2\pi$", r"$4\pi$"))
plt.show()