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
from multiprocessing import Pool

# Définition des constantes du système
omega = 2*np.pi      # Fréquence angulaire
omega0 = 1.5*omega   # Fréquence naturelle du pendule
beta = omega0/4      # Coefficient d'amortissement

# Définition de l'équation différentielle du pendule avec un terme de forçage
def fun(t, x, gamma):  # Ajoutez gamma comme terme de forçage
    phi, phipoint = x[0], x[1]
    v = phipoint
    a = -2*beta*phipoint - omega0**2*np.sin(phi) + gamma*omega0**2*np.cos(omega*t)
    return v, a

t_max = 80          
N_pas = 1000        
N_points = 10       
t = np.arange(t_max - N_points, t_max)
# On crée une liste de valeurs de gamma pour lesquelles on va résoudre l'équation différentielle
liste_gamma = np.arange(1.06, 1.1, 0.0001)

# Cette fonction résout l'équation différentielle pour une valeur donnée de gamma
def compute_gamma(gamma):
    y0 = [0, 0]  # Conditions initiales
    # On résout l'équation différentielle avec la valeur de gamma donnée
    sol = solve_ivp(lambda t, x: fun(t, x, gamma), [0, t_max], y0, t_eval=np.linspace(0., t_max, N_pas), rtol=1e-9, dense_output=True)
    gammas = [gamma] * N_points
    thetas = list((sol.sol(t)[0]+np.pi)%(2*np.pi)-np.pi)
    return gammas, thetas

if __name__ == '__main__':
    with Pool() as p:
        results = []
         # On résout l'équation différentielle pour chaque valeur de gamma dans liste_gamma
        for i, result in enumerate(p.imap(compute_gamma, liste_gamma)):
            results.append(result)
            print(f"\rProgress: {(i+1)/len(liste_gamma)*100:.2f}%", end="")

    # On récupère les résultats
    gammas, thetas = zip(*results)
    gammas = [item for sublist in gammas for item in sublist]
    thetas = [item for sublist in thetas for item in sublist]

    plt.scatter(gammas, thetas, c='black', s=1)
    plt.ylim(-1.5, 0)
    plt.show()
