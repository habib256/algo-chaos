import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

NBPASMAX = 100
nbobject = 64

pos=np.zeros((nbobject,3,NBPASMAX))

objectNb = 0
for i in range(-20,20,10):
    for j in range(-20,20,10):
        for k in range(-20,20,10):
            pos[objectNb][0][0] = i 
            pos[objectNb][1][0] = j 
            pos[objectNb][2][0] = k 
            objectNb = objectNb + 1
    
for i in range(0, nbobject) :
    ax.scatter(pos[i][0][0], pos[i][1][0], pos[i][2][0])
plt.show()
