import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

NBPASMAX = 100
OBJETMAX = 64

pos=np.zeros((OBJETMAX,3,NBPASMAX))

objectNb = 0
for i in range(-20,20,10):
    for j in range(-20,20,10):
        for k in range(-20,20,10):
            pos[objectNb][0][0] = i 
            pos[objectNb][1][0] = j 
            pos[objectNb][2][0] = k 
            objectNb = objectNb + 1

xs = []
ys = []
zs = []

for i in range (0,64) :
    xs.append(pos[i][0][0])
    ys.append(pos[i][1][0])
    zs.append(pos[i][2][0])

ax.scatter(xs, ys, zs)
plt.show()
