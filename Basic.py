import matplotlib.pyplot as plt
import numpy as np

max = 6.3
step = 0.1

x = np.arange(1, max, step)  
y = np.sin(x)  
   
plt.scatter(x,y)
plt.show()