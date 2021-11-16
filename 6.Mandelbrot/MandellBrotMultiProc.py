import numpy as np
import multiprocessing as mp
import time
import plotly.express as px

def equation(rr,ii,ittMax=50):
    itt =0
    N = complex(0,0)
    P = N+1
    C = complex(rr,ii)
    while abs(N) < 1e6 and itt <50 :
        P = N
        N = N**2+C
        itt += 1
    return itt

resolution = 4000
x = np.linspace(-2.0,0.6,resolution)
y = np.linspace(-1.1,1.1,resolution)
XX, YY = np.meshgrid(x,y)

def mapto(pair):
    return equation(XX[pair], YY[pair])

pairs = [(xx,yy) for xx in range(0,resolution) for yy in range(0,resolution)]

deathPool = mp.Pool(processes=4)

print("--Calcul --")
debut = time.time()
#res = list(map(mapto,pairs))
res = list(deathPool.map(mapto,pairs))
fin = time.time()
print("-- Terminé --")
print(str(fin-debut)+" secondes pour l'execution")

res = np.array(res)
z = np.split(res,resolution)

fig = px.imshow(z)
fig.show()